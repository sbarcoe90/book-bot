def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()   

def get_num_words(book_text):
    return len(book_text.split())
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)

    print(f"Found {num_words} total words")

main()