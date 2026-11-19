from scipy.io import loadmat
import numpy as np

mat = loadmat("B0005.mat")
print("Keys:", list(mat.keys()))
print("B0005 shape:", mat["B0005"].shape)
print("B0005 dtype names:", mat["B0005"].dtype.names)

a = mat["B0005"]
print("a shape:", a.shape)
print("a[0][0] shape:", a[0][0].shape)
print("a[0][0] dtype names:", a[0][0].dtype.names)

b = a[0][0]["cycle"]
print("cycle shape:", b.shape)
print("cycle[0] shape:", b[0].shape)
print("cycle[0][0] shape:", b[0][0].shape)

c = b[0][0]
print("c dtype names:", c.dtype.names)
print("c type:", c["type"])
print("c data shape:", c["data"].shape)