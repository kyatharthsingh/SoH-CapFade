from scipy.io import loadmat
import numpy as np

mat = loadmat("B0005.mat")
cycles = mat["B0005"]["cycle"][0]
print("Total cycles:", len(cycles))

for i in range(min(10, len(cycles))):
    c = cycles[i][0][0]
    typ = str(c["type"][0])
    data = c["data"][0][0]
    print(i, "type=", typ, "data_fields=", data.dtype.names)

count_cap = 0
for i in range(len(cycles)):
    c = cycles[i][0][0]
    data = c["data"][0][0]
    if "Capacity" in data.dtype.names:
        count_cap += 1
        if count_cap == 1:
            print("First Capacity cycle index:", i)
            print("Capacity value:", data["Capacity"])
            print("Capacity shape:", np.array(data["Capacity"]).shape)

print("Total cycles WITH Capacity:", count_cap)