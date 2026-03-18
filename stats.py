def get_num_words(text):
    return len(text.split())

def get_char_count(text):
    lowered_text = text.lower()
    char_counts = {}

    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_counts):
    chars = []

    for char, count in char_counts.items():
        chars.append({"char": char, "num": count})

    chars.sort(key=sort_on, reverse=True)
    return chars

def sort_on(items):
    return items["num"]

def get_word_count(text):
    words = text.lower().split()
    word_counts = {}

    for word in words:
        word = word.strip(".,!?;:\"'()[]{}")
        if word == "":
            continue

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def sort_word_counts(word_counts):
    words = []

    for word, count in word_counts.items():
        words.append({"word": word, "num": count})

    words.sort(key=sort_on, reverse=True)
    return words
