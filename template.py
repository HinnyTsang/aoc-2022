"""
    AOC 2022 day .
    Hinny Tsang
"""
def question(file: str) -> None:
    """
        file: input file name
    """
    data = open(file, 'r', encoding="utf-8").readlines()

    result = 0

    print(f"{result = }")


if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question(FILE_NAME)
