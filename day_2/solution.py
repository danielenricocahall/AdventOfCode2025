

def count_invalid_ids(id_range: str) -> int:
    start, end = map(int, id_range.split("-"))
    sum_ = 0
    for _id in range(start, end + 1):
        _id = str(_id)
        left, right = _id[:len(_id) // 2], _id[len(_id) // 2:]
        if left == right:
            sum_ += int(_id)
    return sum_

if __name__ == "__main__":
    with open('./puzzle.txt') as fp:
        id_ranges = fp.readline().split(",")
    sum_of_invalid_ids = 0
    for id_range in id_ranges:
        print(id_range)
        sum_of_invalid_ids += count_invalid_ids(id_range)
    print(sum_of_invalid_ids)
