from stats import get_num_words
from stats import counter
    

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()
    

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {get_num_words(book_text)} total words")
    result = counter(book_text)
    print(result)


main()