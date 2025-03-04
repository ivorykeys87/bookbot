from stats import get_character_count, get_word_count

def get_book_text(file_path):
    with open(file_path) as file:
            file_contents = file.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(text)} words found in the document")
    print(get_character_count(text))




main()


