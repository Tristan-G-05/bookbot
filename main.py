def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_num_words

from stats import get_num_letters

def main():
    book_text = get_book_text('books/frankenstein.txt')
    count = f"{get_num_words(book_text)} words found in the document"
    letter_count = get_num_letters(book_text)
    print(count)
    for key in sorted(letter_count.keys()):
        print(f"'{key}': {letter_count[key]}")

main()
# This is a simple script to read and print the contents of a book file.
# It assumes the book file is located in the 'books' directory.
# The function get_book_text reads the file and returns its content.
# The main function calls this to print the text of 'frankenstein.txt'.