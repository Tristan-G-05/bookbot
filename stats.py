def get_num_words(book_text):
    return len(book_text.split())

def get_num_letters(book_text):
    lower_case_text = book_text.lower()
    letter_dict = {}
    for letter in lower_case_text:
        letter_dict[letter] = letter_dict.get(letter, 0) + 1
    return letter_dict

def sort_character_counts(letter_dict):
    result = []
    for letter, count in letter_dict.items():
        new_letter_dict = {"char": letter, "num": count}
        result.append(new_letter_dict)
    result.sort(reverse=True, key=lambda item: item["num"])
    return result