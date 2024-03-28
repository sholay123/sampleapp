import unittest
from models import Book  # Import the model to be tested

class TestBookModel(unittest.TestCase):
    def test_delete_book(self):
        # Assume we have a book with a known ID in the database
        book_id = 1

        # Perform the DELETE operation
        book = Book.objects.get(id=book_id)  # Assuming Book is a Django model
        book.delete()

        # Try to retrieve the deleted book
        with self.assertRaises(Book.DoesNotExist):
            Book.objects.get(id=book_id)
