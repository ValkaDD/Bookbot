from stats import word_count, get_book_text, listofdic
def main():
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")
    sentence = get_book_text("books/frankenstein.txt")
    print(f"Found {word_count(sentence)} total words\n")
    print("--------- Character Count -------\n")
    CharactersList = listofdic(sentence)
    for Character in CharactersList:
        if Character['char'].isalpha():
                print(f"{Character['char']}: {Character['count']}")
    print("============= END ===============")
main()