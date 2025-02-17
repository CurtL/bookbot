def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = len(text.split())

    count_of_chars = char_count(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for char_value in count_of_chars:
        if char_value.isalpha():
            print(f"The '{char_value}' character was found {count_of_chars[char_value]} times")

    print("--- End report ---")


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def char_count(text):
    text = text.lower()
    count_of_chars = {}
    for char in text:
        if char in count_of_chars.keys():
            count_of_chars[char] += 1
        else:
            count_of_chars[char] = 1

    return count_of_chars

if __name__=="__main__":
    main()