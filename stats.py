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