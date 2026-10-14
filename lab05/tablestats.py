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