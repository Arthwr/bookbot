import sys

from stats import get_book_text
from stats import count_words
from stats import count_chars
from stats import sort_chars
from stats import print_sorted


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    sorted_chars = sort_chars(char_count)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    print_sorted(sorted_chars)


main()
