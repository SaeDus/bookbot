import sys
from stats import get_num_words, count_characters, sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]

    print('=' * 12, "BOOKBOT", '=' * 12)
    print(f"Analyzing book found at {path_to_book}...")

    book_contents = get_book_text(path_to_book)

    print('-' * 11, "Word Count", '-' * 11)

    word_count = get_num_words(book_contents)
    print(f"Found {word_count} total words")

    print('-' * 9, "Character Count", '-' * 9)
    character_dict = count_characters(book_contents)
    sorted_dict = sort_dictionary(character_dict)

    for i in sorted_dict:
        if not i["char"].isalpha():
            continue
        
        print(f"{i["char"]}: {i["num"]}")
    
    print('=' * 13, "END", '=' * 13)

main()
