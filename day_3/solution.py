from itertools import combinations


def find_max_joltage(bank: list[int]):
    # brute force
    battery_combos = set(combinations(bank, r=2))
    max_joltage = 0
    for first_battery, second_battery in battery_combos:
        joltage = int(f"{first_battery}{second_battery}")
        max_joltage = max(joltage, max_joltage)
    return max_joltage




if __name__ == "__main__":
    with open("./puzzle.txt") as fp:
        banks = list(map(lambda x: list(str.strip(x)), fp.readlines()))
        banks = [list(map(int, x)) for x in banks]
        max_joltages = [find_max_joltage(bank) for bank in banks]
        print(sum(max_joltages))