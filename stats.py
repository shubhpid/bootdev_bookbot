from typing import TypedDict

class CharacterCount(TypedDict):
    char: str
    num: int


def get_num_value(item: CharacterCount) -> int:
    return item['num']

def sortedDicList(counter: dict[str, int]) -> list[CharacterCount]:
    d = []
    for character, count in counter.items():
        d.append(CharacterCount(char=character, num=count))

    d.sort(key=get_num_value, reverse=True)
    return d

    

def get_num_words(text: str) -> str:
    words = text.split()
    return str(len(words))

def counter(text: str) -> dict[str, int]:
    text = text.lower()
    word_counts = {}
    words = list(text)
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts