from stats import get_character_count, get_word_count, convert_to_list
import sys

 

def get_book_text(file_path):
    with open(file_path) as file:
            file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found",get_word_count(text),"total words")
    print("--------- Character Count -------")
    list = convert_to_list(get_character_count(text))
    for item in list:
         print(f"{item['character']}: {item['count']}")
    print("============= END ===============")
    




main()


