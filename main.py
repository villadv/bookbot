from stats import (
    get_num_words,
    get_char_count,
    sort_char_counts,
    get_word_count,
    sort_word_counts,
)
import sys
import os


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_name = os.path.basename(book_path)

    text = get_book_text(book_path)

    # ----- Word Count -----
    num_words = get_num_words(text)

    # ----- Character Stats -----
    char_counts = get_char_count(text)
    sorted_chars = sort_char_counts(char_counts)

    # ----- Word Stats -----
    word_counts = get_word_count(text)
    sorted_words = sort_word_counts(word_counts)

    # ----- Output -----
    print("\n--- Bookbot Report ---")
    print(f"File: {file_name}")

    print(f"\nTotal words: {num_words:,}")

    # Character Frequency
    print("\nCharacter Frequency:")
    print("-" * 25)

    for item in sorted_chars:
        char = item["char"]
        if not char.isalpha():
            continue

        count = item["num"]
        print(f"{char:<2} : {count:>10,}")

    # Top Words
    print("\nTop 10 Words:")
    print("-" * 25)

    count = 0
    for item in sorted_words:
        word = item["word"]
        num = item["num"]

        if not word.isalpha():
            continue

        print(f"{word:<12} : {num:>10,}")

        count += 1
        if count == 10:
            break

    print("-" * 25)
    print("End of report\n")


main()
