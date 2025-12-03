def read_inputs(filename: str):
    result = []
    with open(filename, 'r') as file:
        result = [input.strip() for input in file.readlines()]
    return result

def rotate(current: int, direction: str, distance: int):
    if direction != 'L' and direction != 'R':
        raise ValueError(f"Invalid direction {direction}")
    
    num_times_hit_zero = distance // 100
    distance %= 100
    previous = current

    if direction == 'L':
        current -= distance
        if current < 0:
            current = current + 100
        if previous != 0 and (current > previous or current == 0):
            num_times_hit_zero += 1
        print(f"current is {current} after left rotation")
    elif direction == 'R':
        current = (current + distance) % 100
        if previous != 0 and (current < previous or current == 0):
            num_times_hit_zero += 1
        print(f"current is {current} after right rotation")
    
    return current, num_times_hit_zero

if __name__ == "__main__":
    inputs = read_inputs("advent1_input")

    password = 0
    current = 50
    for input in inputs:
        current, num_times_hit_zero = rotate(current, input[0], int(input[1:]))
        password += num_times_hit_zero
    
    print(f"The password is {password}")