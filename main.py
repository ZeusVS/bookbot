def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print_report(book_path, word_count, char_count)

def print_report(title, words, chars):
    sorted_chars = dict(sorted(chars.items(),
                               key=lambda item: item[1],
                               reverse = True
                               ))

    print(f"--- Begin report of {title} ---")
    print(f"{words} words found in the document")
    print()
    for char in sorted_chars:
        if char.isalpha():
            print(f"The '{char}' character was found {chars[char]} times")
    print("--- End of report ---")

def get_word_count(text):
    return len(text.split()) 

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
