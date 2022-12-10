"""
    AOC 2022 day 2.
    Hinny Tsang
"""

def paper_scissor_rock(opponent: str, you: str) -> int:
    """
        calculate the score of each match
    """
    MATCH_SCORE = (3, 0, 6)

    opponent = ord(opponent) - ord('A')
    you = ord(you) - ord('X')

    operations = 0
    while you != opponent:
        you = (you + 1) % 3
        operations += 1

    return MATCH_SCORE[operations]

def question2a(file: str) -> None:
    """
       file: input
    """
    CHOOSE_SCORE = {'X': 1, 'Y': 2, 'Z': 3}

    matches = open(file, 'r', encoding="utf-8").readlines()

    score = 0

    for match in matches:
        match = match.strip().split()
        score += paper_scissor_rock(*match) + CHOOSE_SCORE[match[1]]

    print(score)

def paper_scissor_rock_result(opponent: str, goal: str) -> int:
    """
        choose a result to match the goal.
    """
    goal = ord(goal) - ord('X')
    opponent = ord(opponent) - ord('A')
    you = (opponent + goal) % 3
    return you


def question2b(file: str) -> None:
    """
       file: input
    """
    CHOOSE_SCORE = [3, 1, 2]
    MATCH_SCORE = {'X': 0, 'Y': 3, 'Z': 6}

    matches = open(file, 'r', encoding="utf-8").readlines()

    score = 0

    for match in matches:
        match = match.strip().split()
        score += CHOOSE_SCORE[paper_scissor_rock_result(*match)] + MATCH_SCORE[match[1]]

    print(score)


if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question2a(FILE_NAME)
    question2b(FILE_NAME)
