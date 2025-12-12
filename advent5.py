
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

        # Edge case, if the high range number matches one already in the list then
        # the existing number won't actually get removed (since list deletion doesn't include the high_idx).
        # This number needs to be removed so that we don't get duplicate entries. Incrementing the index by 1
        # will ensure this number is removed and no duplicates occur.
        if high_idx < len(fresh_list) and high == fresh_list[high_idx]:
            high_idx += 1
        
        del fresh_list[low_idx:high_idx]
        if high_idx % 2 == 0:
            fresh_list.insert(low_idx, high)
        if low_idx % 2 == 0:
            fresh_list.insert(low_idx, low)
    print(f"Fresh list: {fresh_list}")

    fresh_count = 0
    for low, high in zip(range(0, len(fresh_list) - 1, 2), 
                        range(1, len(fresh_list), 2)):
        print(f"Processing pair ({fresh_list[low]}, {fresh_list[high]})")
        fresh_count += fresh_list[high] - fresh_list[low] + 1
    print(f"Number of fresh ids: {fresh_count}")
