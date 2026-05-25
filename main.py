import sys
from stats import get_num_words
from stats import counter
from stats import sortedDicList
    

def get_book_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()
    

def main():

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
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
    
    sys.exit(0)
    

main()