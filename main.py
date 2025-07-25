def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_num_words

from stats import get_num_letters

from stats import sort_character_counts

import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_text = get_book_text(sys.argv[1])
    letter_count = get_num_letters(book_text)
    sorted_counts = sort_character_counts(letter_count)
    
    book_found = f"Analyzing book found at {sys.argv[1]}"
    print("============ BOOKBOT ============")
    print(book_found)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
# This is a simple script to read and print the contents of a book file.
# It assumes the book file is located in the 'books' directory.
# The function get_book_text reads the file and returns its content.
# The main function calls this to print the text of 'frankenstein.txt'.