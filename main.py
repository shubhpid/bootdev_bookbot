from stats import get_num_words
from stats import counter
from stats import sortedDicList
    

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()
    

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    result = counter(book_text)
    sorted_results = sortedDicList(result)
    for item in sorted_results:

        if not item['char'].isalpha():
            continue
            print(f"The 'space' character was found {item['num']} times")
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()