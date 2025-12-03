from collections import deque

def read_banks(filename: str):
    banks = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            banks.append([int(num) for num in line.strip()])
    return banks

if __name__ == "__main__":
    joltage = 0
    for bank in read_banks("advent3_input"):
        start_battery = max(bank[:-1])
        end_battery = max(bank[bank.index(start_battery) + 1:])
        print(f"Joltage for bank {bank} is: {start_battery}{end_battery}")
        joltage += (start_battery * 10) + end_battery
    print(f"The joltage is {joltage}")