def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    my_dict = {}
    book_text_lower = book_text.lower()

    for char in book_text_lower:

        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    return my_dict   

def sort_on(d):
    return d["num"]        

def chars_dict_to_sorted_list(num_chars):
    dict_list = []

    for ch in num_chars:
        dict_list.append({"char": ch, "num": num_chars[ch]})

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list


