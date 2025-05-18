import re
from collections import Counter

def get_num_words(file_contents: str) -> int:
    word_count: int = len(re.findall(f'\S+', file_contents))
    return word_count

def get_char_map(file_contents: str) -> dict:
    char_map: dict = Counter(file_contents.lower())
    return char_map

def get_sorted_char_nums(char_map: dict) -> list[dict]:
    sorted_char_nums: list[dict] = []
    base_list = [[k,v] for k,v in char_map.items() if k.isalpha()]
    sorted_list = sorted(base_list, key=lambda e: e[1], reverse=True)
    for e in sorted_list:
        sorted_char_nums.append({'char': e[0], 'num': e[1]})

    return sorted_char_nums