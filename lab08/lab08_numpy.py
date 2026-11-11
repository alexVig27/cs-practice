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


matrix = np.arange(1, 26).reshape(5, 5)
print('первые три строки:', matrix[:3, :])
print( matrix[:3, :].shape)
print('последние две строки:', matrix[3:, :])
print( matrix[3:, :].shape)
print('первые два столбца:', matrix[:, :2])
print(matrix[:, :2].shape)
print('фрагмент из строк с индексами 1–3 и столбцов 2–4:', matrix[1:4, 2:5])
print(matrix[1:4, 2:5].shape)
print('угловой блок 2×2 в правом нижнем углу', matrix[3:, 3:])
print(matrix[3:, 3:].shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9


changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1
print('changed_hours:', changed_hours.tolist())
print('hours:', hours) #.copy() нужна для того чтобы не менять исходный массив.
changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print('changed_matrix:', changed_matrix)
print('matrix:', matrix)