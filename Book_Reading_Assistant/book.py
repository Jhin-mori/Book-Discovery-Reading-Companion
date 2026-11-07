class Book:

    def __init__(self, title, authors, isbn=None,
                 first_publish_year=None, subjects=None,
                 page_count=None, cover_image=None):

        self.title = title
        self.authors = authors
        self.isbn = isbn
        self.first_publish_year = first_publish_year
        self.subjects = subjects
        self.page_count = page_count
        self.cover_image = cover_image

    def display_info(self):

        print("\n----- BOOK INFORMATION -----")

        print(f"Title: {self.title}")
        print(f"Author(s): {', '.join(self.authors)}")
        print(f"ISBN: {self.isbn or 'Not available'}")
        print(f"Publication Year: {self.first_publish_year or 'Not available'}")
        print(f"Subjects: {', '.join(self.subjects or []) or 'Not available'}")
        print(f"Page Count: {self.page_count or 'Not available'}")

        print("----------------------------")

    def get_cover_url(self):

        if self.cover_image:
            return self.cover_image

        if self.isbn:
            return f"https://covers.openlibrary.org/b/isbn/{self.isbn}-L.jpg"

        return None

    def to_dict(self):

        return {
            "title": self.title,
            "authors": self.authors,
            "isbn": self.isbn,
            "first_publish_year": self.first_publish_year,
            "subjects": self.subjects,
            "page_count": self.page_count,
            "cover_image": self.get_cover_url()
        }