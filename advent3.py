from collections import deque

def read_banks(filename: str):
    banks = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            banks.append([int(num) for num in line.strip()])
    return banks

def find_batteries_to_activate(bank: list[int], num_to_activate: int):
    active_batteries = []
    start_idx = 0
    for num_remaining in range(num_to_activate, 0, -1):
        bank_slice = bank[start_idx:(len(bank) - num_remaining + 1)]
        battery = max(bank_slice)
        start_idx += bank_slice.index(battery) + 1
        active_batteries.append(battery)
    return active_batteries

REQUIRED_BATTERY_COUNT = 12

if __name__ == "__main__":
    joltage = 0
    for bank in read_banks("advent3_input"):
        for idx, active_battery in enumerate(find_batteries_to_activate(bank, REQUIRED_BATTERY_COUNT)):
            joltage += active_battery * 10 ** (REQUIRED_BATTERY_COUNT - idx - 1)
    print(f"The joltage is {joltage}")