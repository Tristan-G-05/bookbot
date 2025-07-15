def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

main()
# This is a simple script to read and print the contents of a book file.
# It assumes the book file is located in the 'books' directory.
# The function get_book_text reads the file and returns its content.
# The main function calls this to print the text of 'frankenstein.txt'.