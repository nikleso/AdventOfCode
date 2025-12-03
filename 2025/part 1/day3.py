import os

def max_voltage_2_digits(bank_str):
    if len(bank_str) < 2:
        return 0
    max_val = 0
    for i in range(len(bank_str)):
        for j in range(i + 1, len(bank_str)):
            num = int(bank_str[i] + bank_str[j])
            if num > max_val:
                max_val = num
    return max_val

def max_voltage_12_digits(bank_str):
    if len(bank_str) < 12:
        return 0
    result = []
    n = len(bank_str)
    pos = 0
    for k in range(12):
        end = n - (12 - k)
        max_digit = '0'
        max_idx = pos
        for i in range(pos, end + 1):
            if bank_str[i] > max_digit:
                max_digit = bank_str[i]
                max_idx = i
        result.append(max_digit)
        pos = max_idx + 1
    return int(''.join(result))

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(script_dir, '3.in')
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    total_output_1 = 0
    total_output_2 = 0
    for line in lines:
        total_output_1 += max_voltage_2_digits(line)
        total_output_2 += max_voltage_12_digits(line)
    print(f"Вывод 1: {total_output_1}")
    print(f"Вывод 2: {total_output_2}")

if __name__ == '__main__':
    main()
