from stats import get_num_words, get_num_chars

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()   
    
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)

    print(f"Found {num_words} total words")
    print(f"Found {num_chars} total chars")
    
main()