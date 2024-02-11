def main():
    book_path = "books/frankenstein.txt"
    book = fetch_contents(path=book_path)
    word_count = count_total_words(book)
    letter_count = count_letters(book)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document\n")
    for letter in letter_count:
        print(f"The {letter["letter"]} character was found {letter["count"]} times")
    print(f"--- End Report ---")

def fetch_contents(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_total_words(s):
    return len(s.split())

def count_letters(s) -> list:
    letter_count = {}
    for char in s:
        if char.lower() in letter_count:
            letter_count[char.lower()] += 1
        else:
            letter_count[char.lower()] = 1
    
    # Function key for sort() method
    def sort_func(d):
        return d["count"]
    # Sorts letters that were counted by highest to lowest
    sorted_list = []
    for letter in letter_count:
        if letter.isalpha():
            sorted_list.append({"letter":letter, "count":letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_func)
    return sorted_list


if __name__ == "__main__":
    main()