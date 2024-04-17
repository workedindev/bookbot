def get_book_text(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def get_word_count(string: str) -> int:
    words = string.split()
    return len(words)

def get_letter_dict(string: str) -> dict[str, int]:
    letter_counts = dict()

    for letter in string:
        lowered = letter.lower()
        if lowered in letter_counts:
            letter_counts[lowered] += 1
        else:
            letter_counts[lowered] = 1

    return letter_counts

def letters_sort(dictionary):
    return dictionary["name"]

def letter_dict_to_sorted_list(letter_dict: dict[str, int]) -> list[dict[str, str|int]]:
    letter_list = []
    for letter, count in letter_dict.items():
        if not letter.isalpha():
            continue
        letter_list.append({
            "name": letter,
            "count": count
        })
    letter_list.sort(key=letters_sort)
    return letter_list

def generate_report(book_path: str) -> str:
    report = f"--- Begin report of {book_path} ---\n"
    book_text = get_book_text(book_path)

    word_count = get_word_count(book_text)
    report += f"{word_count} words found in the document\n"

    letter_dict = get_letter_dict(book_text)
    letters = letter_dict_to_sorted_list(letter_dict)
    letters.sort(key=letters_sort)

    for letter in letters:
        report += f"The '{letter['name']}' character was found {letter['count']} times\n"

    report += "--- End report ---\n"
    return report

def main():
    book_path = "books/frankenstein.txt"
    report = generate_report(book_path)
    print(report)

if __name__ == "__main__":
    main()