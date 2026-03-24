def get_num_words(book_text):
    return len(book_text.split())

def get_num_chars(book_text):
    dict = {}
    book_text_lower = book_text.lower()
     # for each char, count +=1
     # Place it in dict
    count = 0
    for c in book_text_lower:
        if c in book_text_lower:
            count += 1
            dict = {c, count}
            print(f"dict:: {dict}")
        else:
            pass
    return dict