def read_inputs(filename: str):
    with open(filename, 'r') as file:
        return file.read().split(',')
    return []

def is_invalid(id: str):
    invalid = False
    for pattern_len in range(len(id) // 2, 0, -1):
        if len(id) % pattern_len != 0:
            continue
        
        parts = set()
        for start_idx, end_idx in zip(range(0, len(id), pattern_len),
                                      range(pattern_len, len(id) + 1, pattern_len)):
            parts.add(id[start_idx:end_idx])
        if  len(parts) == 1:
            print(f"{num} is an invalid number!")
            invalid = True
            break
    return invalid

if __name__ == "__main__":
    sum = 0
    inputs = read_inputs("advent2_input")
    for input in inputs:
        lower, upper = input.split('-')
        for num in range(int(lower), int(upper) + 1):
            if is_invalid(str(num)):
                sum += num
    print(f"Sum is {sum}")
