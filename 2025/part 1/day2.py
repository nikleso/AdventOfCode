import os

def is_invalid_id_part1(n):
    s = str(n)
    length = len(s)
    for part_len in range(1, length // 2 + 1):
        if length != 2 * part_len:
            continue
        part = s[:part_len]
        if len(part) > 1 and part[0] == '0':
            continue
        if part + part == s:
            return True
    return False

def is_invalid_id_part2(n):
    s = str(n)
    length = len(s)
    for part_len in range(1, length // 2 + 1):
        if length % part_len != 0:
            continue
        num_parts = length // part_len
        if num_parts < 2:
            continue
        part = s[:part_len]
        if len(part) > 1 and part[0] == '0':
            continue
        if part * num_parts == s:
            return True
    return False

def parse_ranges(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    ranges = []
    for range_str in content.split(','):
        range_str = range_str.strip()
        if not range_str:
            continue
        start, end = map(int, range_str.split('-'))
        ranges.append((start, end))
    return ranges

def calculate_sum(ranges, check_func):
    total = 0
    for start, end in ranges:
        for n in range(start, end + 1):
            if check_func(n):
                total += n
    return total

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, '2.in')
    ranges = parse_ranges(filename)
    sum_part1 = calculate_sum(ranges, is_invalid_id_part1)
    sum_part2 = calculate_sum(ranges, is_invalid_id_part2)
    print(f"Вывод 1: {sum_part1}")
    print(f"Вывод 2: {sum_part2}")

if __name__ == '__main__':
    main()
