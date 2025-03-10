class Library:
    def __init__(self,books):
        self.books=books
        print("   Welcome To Library!   ")

    def display_books(self):
        print("\n Book availble in the library: ")
        for book in self.books:
            print(f"-{book}")
        print()

    def borrow_book(self,books):
        if book in self.books:


