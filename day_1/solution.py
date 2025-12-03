DIAL_MAX = 100


def rotate_dial(start: int, rotation: str):
    # *sigh* hitting too many edge cases, ai to the rescue. was only 3 off too
    # but i had already done several submissions
    direction, distance = rotation[0], int(rotation[1:])

    if direction == "R":
        base = (-start) % DIAL_MAX
        end = (start + distance) % DIAL_MAX
    else:
        base = start % DIAL_MAX
        end = (start - distance) % DIAL_MAX

    if base == 0:
        first = DIAL_MAX
    else:
        first = base

    if first > distance:
        zero_hits = 0
    else:
        zero_hits = 1 + (distance - first) // DIAL_MAX

    return end, zero_hits


def count_times_dial_points_to_zero(starting_number: int, rotations: list[str]):
    current_number = starting_number
    total_zero_clicks = 0
    total_zero_landings = 0
    for rotation in rotations:
        current_number, zero_hits = rotate_dial(current_number, rotation)
        total_zero_clicks += zero_hits
        if current_number == 0:
            total_zero_landings += 1

    return total_zero_landings, total_zero_clicks


if __name__ == "__main__":
    with open('./puzzle.txt') as fp:
        rotations = list(map(str.strip, fp.readlines()))
    starting_number = 50
    print(count_times_dial_points_to_zero(starting_number, rotations))
