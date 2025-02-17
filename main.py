def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = len(text.split())

    print(word_count)


def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


if __name__=="__main__":
    main()