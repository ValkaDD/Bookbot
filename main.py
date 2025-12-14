from stats import word_count, get_book_text, character_count
def main():
    sentence = get_book_text("books/frankenstein.txt")
    print(f"Found {word_count(sentence)} total words")
    CharactersList = character_count(sentence)
    print(CharactersList)
main()