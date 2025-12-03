DIAL_MAX = 100


def rotate_dial(start: int, rotation: str):
    number_of_zero_crossings = 0
    direction, distance = rotation[0], int(rotation[1:])
    if distance > DIAL_MAX:
        number_of_zero_crossings += distance // DIAL_MAX
        distance = distance % DIAL_MAX
    if direction == "L":
        distance *= -1
    result = start + distance
    if result < 0:
        return result + DIAL_MAX, number_of_zero_crossings + 1
    if result >= DIAL_MAX:
        return result - DIAL_MAX, number_of_zero_crossings + 1
    return result, number_of_zero_crossings


def count_times_dial_points_to_zero(starting_number: int, rotations: list[str]):
    current_number = starting_number
    total_landing_on_zero = 0
    total_number_of_zero_crossings = 0
    for rotation in rotations:
        current_number, number_of_zero_crossings = rotate_dial(current_number, rotation)
        if current_number == 0:
            total_landing_on_zero += 1
        total_number_of_zero_crossings += number_of_zero_crossings
    return total_landing_on_zero, total_number_of_zero_crossings


if __name__ == "__main__":
    with open('./puzzle.txt') as fp:
        rotations = list(map(str.strip, fp.readlines()))
    starting_number = 50
    print(count_times_dial_points_to_zero(starting_number, rotations))
