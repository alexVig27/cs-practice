import numpy as np
def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.array(values)
    if arr.size % width != 0 or width <= 0:
        return []
    b = arr.reshape(arr.size//width, width)
    return np.round(b, 6).tolist()