from stats import get_num_words, get_char_count, sort_char_counts
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)

    print(f"Found {num_words} total words")
    
    char_counts = get_char_count(text)
    sorted_chars = sort_char_counts(char_counts)
    
    for item in sorted_chars:
        char = item["char"]
        if not char.isalpha():
            continue
        print(f"{char}: {item['num']}")

main()
