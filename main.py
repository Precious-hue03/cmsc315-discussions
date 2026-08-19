class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")


class Novel(Book):
    store_name = "Generic Bookstore"

    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
        self.categories = []

    def add_category(self, category: str):
        self.categories.append(category)

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author},"
              f" Pages: {self.page_count}, Store: {self.store_name},"
              f" Categories: {self.categories}")


# --- Demonstration code ---
if __name__ == "__main__":
    b = Book("The Great Gatsby", "F. Scott Fitzgerald")
    b.display_info()

    n = Novel("The Lightning Thief", "Rick Riordan", 377)
    n.add_category("Fantasy")
    n.add_category("Adventure")
    n.display_info()

    n2 = Novel("The Hobbit", "J.R.R. Tolkien", 310)
    n2.display_info()

    Novel.store_name = "Random Bookstore"
    n.display_info()
    n2.display_info()
