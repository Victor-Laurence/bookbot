def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_dict_of_chars(text):
    chars_dict = {}
    words = text.lower().split()
    for word in words:
        for char in word:
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict


def sort_dict_on_value(dict, ascending=True):
    return sorted(list(dict), key=dict.get, reverse=(not ascending))


def get_char_report(char_dict):
    report = []
    for char in sort_dict_on_value(char_dict, False) :
        if char.isalpha():
            report.append(f"The '{char}' character was found {char_dict[char]} times")
    return report


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    word_count = get_word_count(text)
    char_dict = get_dict_of_chars(text)
    char_report = get_char_report(char_dict)

    print(f"--- Begin report of {path}---")
    print(f"{word_count} words found in the document")
    print("")
    for report_line in char_report:
        print(report_line)
    print("--- End report ---")

main()