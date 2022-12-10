"""
    AOC 2022 day 1.
    Hinny Tsang
"""

def question1a(file: str) -> None:
    """
       file: input
    """
    calories = open(file, 'r', encoding="utf-8").readlines()

    max_elf_carry = 0
    elf_carry = 0

    for calory in calories:
        if calory == '\n':
            max_elf_carry = max(max_elf_carry, elf_carry)
            elf_carry = 0
        else:
            elf_carry += int(calory.strip())

    print(max_elf_carry)


def question1b(file: str) -> None:
    """
       file: input
    """
    calories = open(file, 'r', encoding="utf-8").readlines()

    elves_carry = []
    elf_carry = 0

    for calory in calories:
        if calory == '\n':
            elves_carry += [elf_carry]
            elf_carry = 0
        else:
            elf_carry += int(calory.strip())

    elves_carry.sort()
    
    print(sum(elves_carry[-3:]))


if __name__ == "__main__":
    FILE_NAME = './input-a.txt'
    question1a(FILE_NAME)
    question1b(FILE_NAME)