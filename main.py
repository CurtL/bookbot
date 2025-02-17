def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = len(text.split())

    count_of_chars = char_count(text)

    print(count_of_chars)


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