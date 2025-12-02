
def rotate_dial(start: int, rotation: str):
    direction, distance = rotation[0], int(rotation[1:])
    if distance > 100:
        distance = distance % 100
    if direction == "L":
        distance *= -1
    result = start + distance
    if result < 0:
        return result + 100
    if result > 99:
        return result - 100
    return result


def count_times_dial_points_to_zero(starting_number: int, rotations: list[str]):
    current_number = starting_number
    total = 0
    for rotation in rotations:
        current_number = rotate_dial(current_number, rotation)
        if current_number == 0:
            total += 1
    return total


if __name__ == "__main__":
    with open('./puzzle.txt') as fp:
        rotations = list(map(str.strip, fp.readlines()))
    starting_number = 50
    print(count_times_dial_points_to_zero(starting_number, rotations))


