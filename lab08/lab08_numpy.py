import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2,3), -1)
identity = np.eye(3, 3)


print('hours:', hours.tolist(), hours.shape, hours.ndim, hours.size, hours.dtype)
print('line:', line.tolist(), line.shape, line.ndim, line.size, line.dtype)
print('zeros:', zeros.tolist(), zeros.shape, zeros.ndim, zeros.size, zeros.dtype)
print('unknown_table:', unknown_table.tolist(), unknown_table.shape, unknown_table.ndim, unknown_table.size, unknown_table.dtype)
print('identity', identity.tolist(), identity.shape, identity.ndim, identity.size, identity.dtype)


print(f'Третий элемент: {hours[2]}, последний элемент: {hours[-1]}, элементы с индексами 2–5: {hours[2:6].tolist()}, каждый второй элемент: {hours[::2]}, массив в обратном порядке: {hours[::-1]}')


temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print('форма:', temperatures.shape)
print('число измерений:', temperatures.ndim)
print('число элементов:', temperatures.size)
print('значение из второй строки и третьего столбца:', temperatures[1,2])
print('первая строка:', temperatures[0])
print('последний столбец:', temperatures[:, -1])
print('первые две строки без первого столбца:', temperatures[:2, 1:])
print('центральный фрагмент 2×2', temperatures[:2, 1:3])

