from itertools import combinations


def find_max_joltage(bank: list[int], friction: bool = False):
    # brute force
    r = 2 if not friction else 12
    battery_combos = set(combinations(bank, r=r))
    max_joltage = 0
    for batteries in battery_combos:
        joltage = int("".join(map(str, batteries)))
        max_joltage = max(joltage, max_joltage)
    return max_joltage




if __name__ == "__main__":
    with open("./puzzle_test.txt") as fp:
        banks = list(map(lambda x: list(str.strip(x)), fp.readlines()))
        banks = [list(map(int, x)) for x in banks]
        max_joltages = [find_max_joltage(bank, friction=True) for bank in banks]
        print(sum(max_joltages))