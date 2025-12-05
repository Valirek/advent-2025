def read_grid(filename: str):
    grid = []
    with open(filename, 'r') as file:
        for row in file.readlines():
            grid.append([spot for spot in row.strip()])
    return grid

def get_adjacent_rolls(grid: list[str][str], pos: tuple[int, int]):
    num_adj = 0
    row, col = pos
    for d_row, d_col in [(-1, 0), (-1, 1), (0, 1), (1, 1), 
                    (1, 0), (1, -1), (0, -1), (-1, -1)]:
        new_row, new_col = (row + d_row, col  + d_col)
        if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[row]):
            continue
        if grid[new_row][new_col] == '@':
            num_adj += 1
    return num_adj

def remove_rolls(grid: list[str][str]) -> tuple[list[str][str], int]:
    rolls_removed = 0
    modified_grid = grid.copy()
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] != '@':
                continue
            if get_adjacent_rolls(grid, (row, col)) < 4:
                modified_grid[row][col] = '.'
                rolls_removed += 1
    return modified_grid, rolls_removed

if __name__ == '__main__':
    grid = read_grid('advent4_input')

    rolls_removed = 0
    while True:
        grid, rolls_removed_this_pass = remove_rolls(grid)
        if rolls_removed_this_pass == 0:
            break
        rolls_removed += rolls_removed_this_pass
    print(f"Number of removable rolls: {rolls_removed}")
