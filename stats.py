def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()

    return text


def count_words(text):
    words = text.split()

    return len(words)


def count_chars(text):
    char_counts = {}

    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


def sort_chars(source_dict):
    sorted_list = []

    def sort_on(item):
        return item["count"]

    for char, count in source_dict.items():
        char_count = {
            "character": char,
            "count": count,
        }

        sorted_list.append(char_count)

    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list


def print_sorted(char_list):
    for item in char_list:
        char = item["character"]
        count = item["count"]

        if char.isalpha():
            print(f"{char}: {count}")
