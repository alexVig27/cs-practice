def winner(names: list[str], scores: list[float]) -> str:
    max_res = 0
    name_win = names[0]
    for i in range(1, len(scores)):
        if abs(scores[i]) > max_res:
            max_res = scores[i]
            name_win = names[i]
    return name_win