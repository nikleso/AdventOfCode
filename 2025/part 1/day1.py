import os

def load_input():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, '1.in')
    with open(filepath, 'r', encoding='utf-8') as f:
        data = [line.strip() for line in f if line.strip()]
    return data

def parse(data):
    return [(line[0], int(line[1:])) for line in data]

def part1(data):
    count = 0
    insts = parse(data)
    pos = 50
    for dir, val in insts:
        pos += val if dir == 'R' else -val
        pos %= 100
        if pos == 0:
            count += 1
    return count

def part2(data):
    count = 0
    insts = parse(data)
    pos = 50
    for dir, val in insts:
        for _ in range(val):
            if dir == 'R':
                pos += 1
            else:
                pos -= 1
            if pos == -1:
                pos = 99
            elif pos == 100:
                pos = 0
            if pos == 0:
                count += 1
    return count

def main():
    data = load_input()
    print(f"Вывод 1: {part1(data)}")
    print(f"Вывод 2: {part2(data)}")

if __name__ == '__main__':
    main()
