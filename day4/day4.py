"""
    AOC 2022 day 4.
    Hinny Tsang
"""
def get_boundary(*elfs):
    """
        pair: pair of elves.
    """
    begin = max([elf[0] for elf in elfs])
    end = min([elf[1] for elf in elfs])

    return begin, end

def is_fully_contain(*elfs):
    """
        pair: pair of elves.
    """
    begin, end = get_boundary(*elfs)

    if begin > end:
        return False

    return any([elf == [begin, end] for elf in elfs])

def is_overlap(*elfs):
    """
        pair: pair of elves.
    """
    begin, end = get_boundary(*elfs)

    return begin <= end


def question4a(file: str) -> None:
    """
        file: input file name
    """
    pairs = open(file, 'r', encoding="utf-8").readlines()

    count_fully_contain = 0

    for pair in pairs:

        elfs = [[int(n) for n in pack.split('-')] for pack in pair.split(',')]

        if is_fully_contain(*elfs):
            count_fully_contain += 1

    print(f"{count_fully_contain = }")


def question4b(file: str) -> None:
    """
        file: input file name
    """
    pairs = open(file, 'r', encoding="utf-8").readlines()

    count_overlap = 0

    for pair in pairs:

        elfs = [[int(n) for n in pack.split('-')] for pack in pair.split(',')]

        if is_overlap(*elfs):
            count_overlap += 1

    print(f"{count_overlap = }")



if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question4a(FILE_NAME)
    question4b(FILE_NAME)
