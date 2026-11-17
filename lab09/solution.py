import numpy as np

def make_hours() -> list[int]:
    return np.arange(0,22, 3).tolist()

def vector_report(values: list[float]) -> dict:
    arr = np.array(values)
    return {'третий срез': arr[2].item(),
            'последний срез': arr[-1].item(),
            'средний срез': arr[2:6].tolist(),
            'каждый второй': arr[::2].tolist(),
            'развёрнутый вектор': arr[::-1].tolist(),
            }