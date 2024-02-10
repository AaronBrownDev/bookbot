def main():
    book_path = "books/frankenstein.txt"
    book = fetch_contents(path=book_path)
    word_count = count_total_words(book)
    letter_count = count_letters(book)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document")
    print(letter_count)

def fetch_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_total_words(s):
    return len(s.split())

def count_letters(s) -> dict:
    letter_count = {}
    for char in s:
        if char.lower() in letter_count:
            letter_count[char.lower()] += 1
        else:
            letter_count[char.lower()] = 1
    return letter_count




if __name__ == "__main__":
    main()