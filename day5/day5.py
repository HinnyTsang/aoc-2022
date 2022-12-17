"""
    AOC 2022 day 5.
    Hinny Tsang
"""
import re

def move_crate_at_the_same_time(crates, move):
    """
        crates: crates
        move: current move
    """
    steps, begin, end = move
    crate_to_move = []

    for _ in range(steps):
        if len(crates[begin - 1]) == 0:
            break
        crate_to_move.append(crates[begin - 1].pop())

    crate_to_move.reverse()
    crates[end - 1] += crate_to_move

def move_crate_one_by_one(crates, move):
    """
        crates: crates
        move: current move
    """
    steps, begin, end = move
    for _ in range(steps):
        crates[end - 1].append(crates[begin - 1].pop())

def get_crates_and_moves(crates_and_moves):
    """
        crates_and_moves: input texts.
    """
    n_crates = len(crates_and_moves[0]) // 4
    seperator = crates_and_moves.index('\n')
    crates = [[] for _ in range(n_crates)]
    moves = []

    # fill crates
    for i in range(seperator - 2, -1, -1):
        crates_in_level = [crates_and_moves[i][j:j+4].strip() for j in range(0, 4 * n_crates, 4)]
        for crate_container, crate in zip(crates, crates_in_level):
            if crate != '':
                crate_container.append(crate[1])

    # fill moves
    for i in range(seperator + 1, len(crates_and_moves)):
        move = crates_and_moves[i].strip()
        move = [int(_) for _ in re.findall(r'\d+', move)]
        moves.append(move)

    return crates, moves

def question5a(file: str) -> None:
    """
        file: input file name
    """
    crates_and_moves = open(file, 'r', encoding="utf-8").readlines()

    crates, moves = get_crates_and_moves(crates_and_moves)

    for move in moves:
        move_crate_one_by_one(crates, move)

    tp_of_stack = ''.join([crate[-1] if len(crate) > 0 else ' ' for crate in crates])

    print(f"{tp_of_stack = }")

def question5b(file: str) -> None:
    """
        file: input file name
    """
    crates_and_moves = open(file, 'r', encoding="utf-8").readlines()

    crates, moves = get_crates_and_moves(crates_and_moves)

    for move in moves:
        move_crate_at_the_same_time(crates, move)

    tp_of_stack = ''.join([crate[-1] if len(crate) > 0 else ' ' for crate in crates])

    print(f"{tp_of_stack = }")


if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question5a(FILE_NAME)
    question5b(FILE_NAME)
