from open_library import OpenLibraryClient
from book import Book

client = OpenLibraryClient()
title = input("Enter a book title: ")


results = client.search_by_title(title)

if results:
    for index, result in enumerate(results, start=1):
        choice = int(input("Select a book number: "))
        print(index, result.get("title"))
    first_book = results[choice -1]

    book = Book(
        title=first_book.get("title"),
        authors=first_book.get("author_name", []),
        isbn=first_book.get("isbn"),
        first_publish_year=first_book.get("first_publish_year"),
        subjects=first_book.get("subject"),
        page_count=first_book.get("number_of_pages_median"),
        cover_image=first_book.get("cover_i")
    )


    book.display_info()
    print("Cover URL:", book.get_cover_url())
    book_data = book.to_dict()

    print(book_data)

else:
    print("No book found")   