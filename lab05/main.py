import sys
import tablestats

def main():
    table_name = sys.stdin.readline().strip()
    with open(table_name, "r", encoding="utf-8") as table:
        lines = table.readlines()
    rows = tablestats.read_rows(lines)
    total_rec = len(rows)
    counts = tablestats.count_types(rows)
    unic_types = len(counts)
    error_min = tablestats.total_minutes(rows, "ошибка")
    print(total_rec)
    print(unic_types)
    print(error_min)
    res =tablestats.to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out_file:
        out_file.write(res)

if __name__ == "__main__":
    main()