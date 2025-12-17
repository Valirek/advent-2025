def read_input(filename: str):
    input = []
    with open(filename, 'r') as file:
        for row in file.readlines():
            input.append(row.split())
    return input

def solve(worksheet: list[list[int]], column: int):
    operation = worksheet[-1][col]

    solution = 0
    for row in range(0, len(worksheet) - 1):
        if row == 0:
            solution = int(worksheet[row][col])
            continue

        match operation:
            case '*':
                solution *= int(worksheet[row][col])
            case '+':
                solution += int(worksheet[row][col])
    return solution

if __name__ == '__main__':
    worksheet = read_input('advent6_input')
    grand_total = 0
    for col in range(0, len(worksheet[0])):
        solution = solve(worksheet, col)
        print(f"Column {col} solution is: {solution}")
        grand_total += solution
    print(f"Grand total: {grand_total}")
            
            

