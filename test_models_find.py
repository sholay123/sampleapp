import unittest
from models import Book  # Import the model to be tested

class TestBookModel(unittest.TestCase):
    def test_find_by_name(self):
        # Assume we have a book with a known title in the database
        book_title = "The Great Gatsby"

        # Perform the FIND BY NAME operation
        found_books = Book.objects.filter(title__icontains=book_title)  # Assuming Book is a Django model

        # Assertions
        self.assertIsNotNone(found_books)  # Ensure that at least one book is found
        for book in found_books:
            self.assertTrue(book.title.lower().startswith(book_title.lower()))  # Check if the title matches
