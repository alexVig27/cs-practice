import numpy as np

def make_hours() -> list[int]:
    return np.arange(0,22, 3).tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.array(values, dtype=float)
    return {'third': arr[2].item(),
            'last': arr[-1].item(),
            'middle': arr[2:6].tolist(),
            'every_second': arr[::2].tolist(),
            'reversed': arr[::-1].tolist(),
            }

def change_vector(values: list[float]) -> list[float]:
    arr = np.array(values, dtype=float).copy()
    arr[2:4] = 99
    arr[::2] = -1
    return arr.tolist()


def cap_above(values: list[float], limit: float) -> list[float]:
    arr = np.array(values, dtype=float)
    arr[arr > limit] = limit
    return arr.tolist()

def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    arr = np.array(values, dtype=float)
    c = arr * 9 / 5 + 32
    return c.tolist()