def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()   

def main():
    book_path = "books/frankenstein.txt"
    book1 = get_book_text(book_path)
    print(book1)

main()