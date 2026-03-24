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