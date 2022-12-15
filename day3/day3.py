"""
    AOC 2022 day 3.
    Hinny Tsang
"""
from typing import List
import string

def count_characters(characters: List) -> dict:
    result = {}
    for character in characters:
        if character in result.keys():
            result[character] += 1
        else:
            result[character] = 0

    return result

def intersection(*args) -> List:
    result = []

    counts = [count_characters(item) for item in args]
    
    for alphabet in string.ascii_lowercase + string.ascii_uppercase:
        if all([alphabet in count.keys() for count in counts]):
            result += [alphabet]

    return result

def get_score(alphabet: str) -> int:
    if alphabet in string.ascii_lowercase:
        return ord(alphabet) - ord('a') + 1
    else:
        return ord(alphabet) - ord('A') + 27

def question3a(file: str) -> None:
    compartments = open(file, 'r', encoding="utf-8").readlines()

    shared_items = []
    total_score = 0

    for compartment in compartments:
        
        compartment = compartment.strip()
        n = len(compartment)
        left, right = compartment[:n//2], compartment[n//2:]
        shared_items += [*intersection(left, right)]

    for shared_item in shared_items:
        total_score += get_score(shared_item)

    print(f"{total_score = }")

def question3b(file: str) -> None:
    compartments = open(file, 'r', encoding="utf-8").readlines()

    shared_items = []
    total_score = 0

    n = len(compartments) // 3

    for i in range(n):
        
        indexes = [int(i * 3 + j) for j in range(3)]

        group = [compartments[j].strip() for j in indexes]
        
        shared_items += [*intersection(*group)]

    for shared_item in shared_items:
        total_score += get_score(shared_item)

    print(f"{total_score = }")

if __name__ == "__main__":
    FILE_NAME = './input.txt'
    question3a(FILE_NAME)
    question3b(FILE_NAME)

