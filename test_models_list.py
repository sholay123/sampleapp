from models import Book  # Import the model to be tested

def test_list_all_books():
    # Assume we have multiple books in the database
    expected_books = [
        {"title": "Book 1", "author": "Author 1"},
        {"title": "Book 2", "author": "Author 2"},
        # Add more books as needed
    ]

    # Retrieve all books from the database
    all_books = Book.objects.all()  # Assuming Book is a Django model

    # Assertions
    assert len(all_books) == len(expected_books)  # Ensure the correct number of books is retrieved

    for book, expected_data in zip(all_books, expected_books):
        assert book.title == expected_data["title"]
        assert book.author == expected_data["author"]
