def read_input(filename: str):
    input = []
    with open(filename, 'r') as file:
        for row in file.readlines():
            input.append(row.replace('\n', ''))
    return input

def get_problems(worksheet: list[str]):
    problems = []
    problem = []
    for col in range(0, len(worksheet[0])):
        number_str = ""
        for row in range(0, len(worksheet)):
            if worksheet[row][col] != ' ':
                number_str += worksheet[row][col]
        if number_str:
            problem.append(int(number_str))
        else:
            problems.append(problem)
            problem = []
    if problem:
        problems.append(problem)
    return problems

def solve_problem(problem: list[int], operator: str):
    solution = problem[0]
    for num in problem[1:]:
        match operator:
            case '*':
                solution *= num
            case '+':
                solution += num
    return solution


if __name__ == '__main__':
    worksheet = read_input('advent6_input')

    operators = worksheet[-1].split()
    problems = get_problems(worksheet[:-1])
    
    grand_total = 0
    for problem, operator in zip(problems, operators):
        grand_total += solve_problem(problem, operator)
    print(f"Grand total is {grand_total}")
            
            

