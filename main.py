from stats import word_count, get_book_text, listofdic
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============\n")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------\n")
    sentence = get_book_text(book_path)
    print(f"Found {word_count(sentence)} total words\n")
    print("--------- Character Count -------\n")
    CharactersList = listofdic(sentence)
    for Character in CharactersList:
        if Character['char'].isalpha():
                print(f"{Character['char']}: {Character['count']}")
    print("============= END ===============")
main()