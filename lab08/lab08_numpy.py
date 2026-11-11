import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3), -1)
identity = np.eye(3, 3)


print(hours.tolist(), hours.shape, hours.ndim, hours.size, hours.dtype)
print(line.tolist(), line.shape, line.ndim, line.size, line.dtype)
print(zeros.tolist(), zeros.shape, zeros.ndim, zeros.size, zeros.dtype)
print(unknown_table.tolist(), unknown_table.shape, unknown_table.ndim, unknown_table.size, unknown_table.dtype)
print(identity.tolist(), identity.shape, identity.ndim, identity.size, identity.dtype)