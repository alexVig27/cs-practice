import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.array(values)
    if arr.size % width != 0 or width <= 0:
        return []
    b = arr.reshape(arr.size//width, width)
    return np.round(b, 6).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.array(matrix)
    b = arr[np.ix_(rows, columns)]
    return np.round(b, 6).tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.array(matrix)
    if arr.size == 0:
        return []
    srednee = np.mean(arr, axis=0)
    return np.round(srednee, 6).tolist()