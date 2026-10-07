def winner(names: list[str], scores: list[float]) -> str:
    max_res = 0
    name_win = []
    for i in range(len(scores)):
        if abs(scores[i]) > max_res:
            max_res = scores[i]
            name_win = names[i]
    return name_win


def average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    res = list(names)
    scores_copy = list(scores)
    for i in range(1, len(scores_copy)):
        curr_name = res[i]
        curr_score = scores_copy[i]
        j = i - 1
        while j >= 0 and scores_copy[j] < curr_score:
            scores_copy[j + 1] = scores_copy[j]
            res[j + 1] = res[j]
            j -= 1
        scores_copy[j + 1] = curr_score
        res[j + 1] = curr_name
    return res

def above_average(names: list[str], scores: list[float]) -> list[str]:
    sr_znach = average(scores)
    new_names = []
    for i in range(len(scores)):
        if scores[i] > sr_znach:
            new_names.append(names[i])
    return new_names

if __name__ == '__main__':
    print(winner(["Аня", "Боря", "Вика"], [7.0, 9.0, 18.0]))
