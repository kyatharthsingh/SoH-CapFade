# SoH-CapFade: Capacity Fade Modelling and State of Health Estimation

Predicting the State of Health (SoH) and capacity fade of Lithium-ion batteries using Machine Learning on the 【entity-NASA¦canonical_name=NASA】 Battery Dataset.

## Results

| Model | R2 Score | RMSE |
| --- | --- | --- |
| Linear Regression | 0.9381 | 0.0445 |
| Polynomial Regression | 0.9823 | 0.0238 |
| Random Forest (Best) | 0.9970 | 0.0104 |

Random Forest outperformed traditional regression models by capturing the non-linear degradation pattern of the battery.

## Dataset

- Source: 【entity-NASA¦canonical_name=NASA】 Ames Prognostics Center - Battery B0005
- Total Cycles: 168 charge-discharge cycles
- Capacity Degradation: 2.0Ah to 1.4Ah (down to 70% SoH)
- Features Used: Cycle Number, Measured Voltage, Temperature, Current

## Methodology

1. Data Preprocessing and Cleaning of 【entity-NASA¦canonical_name=NASA】 Battery Data
2. Feature Engineering: Cycle Number, Voltage, Temperature
3. Model Training: Linear Regression, Polynomial Regression, Random Forest
4. Model Evaluation using R2 Score and RMSE
5. Visualization of Actual vs Predicted Capacity Fade

## Tech Stack

Python, Pandas, NumPy, Scikit-Learn, Matplotlib, VS Code

## Applications

- Electric Vehicles (EV) - Predictive Battery Maintenance
- Energy Storage Systems
- Early Detection of Battery Failure
- Battery Remaining Useful Life (RUL) Estimation

## Author

Yatharth Singh
GitHub: https://github.com/kyatharthsingh
LinkedIn: https://www.linkedin.com/in/kyatharthsingh
