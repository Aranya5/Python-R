class Library:
    total_books = 0
    total_users = 0
    total_price = 0.0
    def __init__(self, book_price, book_name="", user_name=""):
        if book_name != "":
            self.book_name = book_name
            self.book_price = book_price
            Library.total_books += 1
            Library.total_price += book_price
        else:
            self.book_name = ""
            self.book_price = 0.0
        if user_name != "":
            self.user_name = user_name
            Library.total_users += 1
        else:
            self.user_name = ""
    def displayb(self):
        if self.book_name != "":
            print(f"Book Name: {self.book_name}, Price: {self.book_price}")
    def displayu(self):
        if self.user_name != "":
            print(f"User Name: {self.user_name}")
    def display():
        print(f"\nTotal Books: {Library.total_books}, "
              f"Total Users: {Library.total_users}, "
              f"Total Price of Books: {Library.total_price}\n")
while True:
    a = input("Enter name of book (or type 'exit' to stop): ")
    if a.lower() == 'exit':
        break
    b = float(input("Enter price of book: "))
    c = input("Enter name of user: ")
    lib = Library(b, a, c)
    lib.displayb()
    lib.displayu()
Library.display()