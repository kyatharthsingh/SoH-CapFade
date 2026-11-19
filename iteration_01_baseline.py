from scipy.io import loadmat
import numpy as np

mat = loadmat("B0005.mat")
print("Keys:", list(mat.keys()))
print("B0005 shape:", mat["B0005"].shape)
print("B0005 dtype:", mat["B0005"].dtype)

cycles = mat["B0005"]["cycle"][0]
print("Total cycles in file:", len(cycles))
print("First cycle type:", cycles[0].dtype)
print("First cycle keys:", cycles[0][0][0].dtype.names)

c0 = cycles[0][0][0]
print("First cycle type value:", c0["type"])
print("First cycle data names:", c0["data"][0][0].dtype.names)
print("First cycle Capacity sample:", c0["data"][0][0]["Capacity"])