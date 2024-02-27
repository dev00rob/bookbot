def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

"""
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
"""
def get_char_count(text):
    low_text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = {}
    for letter in alphabet:
        letters[letter] = 0
    for letter in low_text:
        if alphabet.find(letter) != -1:
            letters[letter] += 1
    return letters 

"""
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""

def get_cc_sorted(cc):
    # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/ 
    return dict(sorted(cc.items(), key=lambda x:x[1], reverse=True))


def get_report(bp, wc, cc):
    result = (f"--- Begin report of {bp} ---\n")
    result += (f"{wc} words found in the document\n\n")
    cc_sorted = get_cc_sorted(cc)
    for c in cc_sorted:
        result += (f"The {c} character was found {cc_sorted[c]} times\n")
    result += "--- End report ---"
    return result
    
def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    report = get_report(book_path, word_count, char_count)
    print(report)

main()

"""
def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

main()
"""