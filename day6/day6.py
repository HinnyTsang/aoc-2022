"""
    AOC 2022 day 6.
    Hinny Tsang
"""

def get_first_marker(signal: str, number_of_distinct: int) -> None:
    """
        signal: str of signal
    """
    first_marker = -1
    count_character = []

    for i, character in enumerate(signal):
        count_character.append(character)
        if len(count_character) > number_of_distinct:
            count_character.remove(signal[i - number_of_distinct])
        if len(count_character) == len(set(count_character)) == number_of_distinct:
            first_marker = i + 1
            break

    return first_marker


def question6a(file: str) -> None:
    """
        file: input file name
    """
    signal = open(file, 'r', encoding="utf-8").readlines()[0]

    first_marker = get_first_marker(signal.strip(), 4)

    print(f"{first_marker = }")

def question6b(file: str) -> None:
    """
        file: input file name
    """
    signal = open(file, 'r', encoding="utf-8").readlines()[0]

    first_marker = get_first_marker(signal.strip(), 14)

    print(f"{first_marker = }")


if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question6a(FILE_NAME)
    question6b(FILE_NAME)
