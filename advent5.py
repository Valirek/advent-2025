
def read_input(filename: str) -> tuple[list[list[int]], list[int]]:
    fresh_ranges = []
    available_ids = []
    with open(filename, 'r') as file:
        before_newline = True
        for line in file.readlines():
            if line == '\n':
                before_newline = False
                continue
            if before_newline:
                fresh_ranges.append([int(val) for val in line.strip().split('-')])
            else:
                available_ids.append(int(line.strip()))
    return fresh_ranges, available_ids

def find_insertion_idx(values: list[int], value: int):
    low = 0
    high = len(values) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if value == values[mid]:
            return mid
        if value < values[mid]:
            high = mid - 1
        elif value > values[mid]:
            low = mid + 1
    return low

if __name__ == '__main__':
    fresh_ranges, ids = read_input('advent5_input')

    fresh_list = []
    for low, high in fresh_ranges:
        low_idx = find_insertion_idx(fresh_list, low)
        high_idx = find_insertion_idx(fresh_list, high)

        del fresh_list[low_idx:high_idx]
        if high_idx % 2 == 0:
            fresh_list.insert(low_idx, high)
        if low_idx % 2 == 0:
            fresh_list.insert(low_idx, low)

    fresh_count = 0
    for id in ids:
        if find_insertion_idx(fresh_list, id) % 2 != 0:
            fresh_count += 1
    print(f"Number of fresh ids: {fresh_count}")
