from typing_extensions import reveal_type


def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None
    for line in lines:
        line = line.rstrip("\n").rstrip("\r")
        if line == "":
            continue
        fds = line.split(",")
        clean_fds = [f.rstrip() for f in fds]
        if header is None:
            header = clean_fds
            continue
        if len(clean_fds) != len(header):
            continue
        row_dict = {}
        for i in range(len(header)):
            row_dict[header[i]] = clean_fds[i]
        rows.append(row_dict)
    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        t_curr = row['тип']
        if t_curr not in counts:
            counts[t_curr] = 1
        else:
            counts[t_curr] += 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    has_kind = False
    for row in rows:
        if row["тип"] == kind:
            has_kind = True
            minuts_str = row["минуты"]
            minuts_str = minuts_str.replace(",", ".")
            is_number = True
            correct_chars = '0123456789.'
            for char in minuts_str:
                if char not in correct_chars:
                    is_number = False
            cnt_dot = 0
            for char in minuts_str:
                if char == ".":
                    cnt_dot += 1
            if cnt_dot > 1 or minuts_str == "" or minuts_str == ".":
                is_number = False

            if is_number:
                total += float(minuts_str)
    if not has_kind:
        return 0.0
    return round(total, 1)


