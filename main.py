import string

def open_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(book_text):
    words = book_text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def count_char_instance(book_text):
    char_count = {char: 0 for char in string.ascii_lowercase}
    text = book_text
    for char in text.lower():
        if char in char_count:
                char_count[char] += 1
    return char_count

def print_report(word_count,char_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    chars = [char for char in string.ascii_lowercase]
    for char in chars:
       print(f"The '{char}' character was found {char_count.get(char)} times")
    print("--- End report ---")

wc = count_words(open_book("books/frankenstein.txt"))
cc = count_char_instance(open_book("books/frankenstein.txt"))
print_report(wc,cc)
