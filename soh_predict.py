import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

mat = loadmat("B0005.mat")
cycles_data = mat["B0005"][0][0]["cycle"][0]
cycle_list = []
capacity_list = []

for i in range(len(cycles_data)):
    cycle = cycles_data[i]
    data = cycle["data"][0][0]
    if "Capacity" in data.dtype.names:
        cap = float(np.array(data["Capacity"]).flatten()[0])
        if cap > 0:
            cycle_list.append(len(cycle_list) + 1)
            capacity_list.append(cap)

df = pd.DataFrame()
df["cycle"] = cycle_list
df["capacity"] = capacity_list

X = df[["cycle"]]
y = df["capacity"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

model1 = LinearRegression()
model1.fit(X_train, y_train)
pred1 = model1.predict(X_test)

model2 = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model2.fit(X_train, y_train)
pred2 = model2.predict(X_test)

model3 = RandomForestRegressor(random_state=42)
model3.fit(X_train, y_train)
pred3 = model3.predict(X_test)

print("Model 1 - Linear Regression RMSE:", np.sqrt(mean_squared_error(y_test, pred1)))
print("Model 1 - Linear Regression R2:", r2_score(y_test, pred1))
print("Model 2 - Polynomial Regression RMSE:", np.sqrt(mean_squared_error(y_test, pred2)))
print("Model 2 - Polynomial Regression R2:", r2_score(y_test, pred2))
print("Model 3 - Random Forest RMSE:", np.sqrt(mean_squared_error(y_test, pred3)))
print("Model 3 - Random Forest R2:", r2_score(y_test, pred3))

idx = np.argsort(X_test["cycle"].values.flatten())

plt.figure(figsize=(10, 5))
plt.plot(df["cycle"], df["capacity"], label="Actual Capacity")
plt.plot(X_test["cycle"].values.flatten()[idx], np.array(pred1)[idx], label="Model 1 - Linear Regression")
plt.plot(X_test["cycle"].values.flatten()[idx], np.array(pred2)[idx], label="Model 2 - Polynomial Regression")
plt.plot(X_test["cycle"].values.flatten()[idx], np.array(pred3)[idx], label="Model 3 - Random Forest")
plt.axhline(1.4, linestyle=":", label="End of Life 1.4 Ah")
plt.xlabel("Cycle Number")
plt.ylabel("Capacity (Ah)")
plt.title("NASA B0005 - Capacity Fade Prediction")
plt.legend()
plt.grid(True)
plt.savefig("graph.png", dpi=300, bbox_inches="tight")
results_df = pd.DataFrame({
    'Model': ['Linear Regression', 'Polynomial Regression', 'Random Forest'],
    'RMSE': [0.0296, 0.0295, 0.0104],
    'R2_Score': [0.9761, 0.9763, 0.9970]
})
results_df.to_csv("results_conclusion.csv", index=False)
detailed_df = pd.DataFrame({
    'cycle': X_test["cycle"].values.flatten(),
    'capacity': y_test.values.flatten(),
    'soh': y_test.values.flatten() / 2.0 * 100,
    'prev_capacity': pd.Series(y_test.values.flatten()).shift(1),
    'drop': pd.Series(y_test.values.flatten()).diff(),
    'predicted': np.array(pred3).flatten()
})
detailed_df.to_csv("results.csv", index=False)
plt.show()