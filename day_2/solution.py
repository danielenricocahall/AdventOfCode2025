

def count_invalid_ids(id_range: str, max_repeats: int | None = None) -> int:

    def are_there_repeats(_id):

        L = len(_id)
        for block_size in range(1, L // 2 + 1):
            if L % block_size != 0:
                continue
            repeats = L // block_size
            if repeats < 2:
                continue
            if max_repeats and repeats != max_repeats:
                continue
            block = _id[:block_size]
            if block * repeats == _id:
                return True
        return False

    start, end = map(int, id_range.split("-"))
    sum_ = 0
    for _id in range(start, end + 1):
        _id = str(_id)
        if are_there_repeats(_id):
            sum_ += int(_id)
    return sum_


if __name__ == "__main__":
    with open('./puzzle.txt') as fp:
        id_ranges = fp.readline().split(",")
    sum_of_invalid_ids = 0
    for id_range in id_ranges:
        sum_of_invalid_ids += count_invalid_ids(id_range, None)
    print(sum_of_invalid_ids)
