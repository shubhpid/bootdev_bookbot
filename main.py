def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()
    
def num_words(text: str) -> str:
    words = text.split()
    return str(len(words))



def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"Found {num_words(book_text)} total words")


main()