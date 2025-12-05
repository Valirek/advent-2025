def read_grid(filename: str):
    grid = []
    with open(filename, 'r') as file:
        for row in file.readlines():
            grid.append([spot for spot in row.strip()])
    return grid

if __name__ == '__main__':
    grid = read_grid('advent4_input')

    accessible_rolls = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] != '@':
                continue

            num_adj = 0
            for d_row, d_col in [(-1, 0), (-1, 1), (0, 1), (1, 1), 
                               (1, 0), (1, -1), (0, -1), (-1, -1)]:
                new_row, new_col = (row + d_row, col  + d_col)
                if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[row]):
                    continue
                if grid[new_row][new_col] == '@':
                    num_adj += 1
            if num_adj < 4:
                accessible_rolls += 1
    print(f"Number of accessible rolls: {accessible_rolls}")
