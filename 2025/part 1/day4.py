def count_initial_accessible(grid, directions):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@':
                neighbor_count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbor_count += 1
                if neighbor_count < 4:
                    count += 1
    return count

def remove_rolls_iteratively(grid, directions):
    rows, cols = len(grid), len(grid[0])
    total_removed = 0
    while True:
        to_remove = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbor_count = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                            neighbor_count += 1
                    if neighbor_count < 4:
                        to_remove.append((r, c))
        if not to_remove:
            break
        for r, c in to_remove:
            grid[r][c] = '.'
        total_removed += len(to_remove)
    return total_removed

def main():
    with open('4.in', 'r') as f:
        grid = [list(line.strip()) for line in f if line.strip()]
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    initial_accessible = count_initial_accessible(grid, directions)
    print("Вывод 1:", initial_accessible)
    total_removed = remove_rolls_iteratively(grid, directions)
    print("Вывод 2:", total_removed)

if __name__ == '__main__':
    main()
