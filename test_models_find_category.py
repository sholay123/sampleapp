from models import Book  # Import the model to be tested

def test_find_by_category():
    # Assume we have books with known categories in the database
    category = "Fiction"

    # Perform the FIND BY CATEGORY operation
    books_in_category = Book.objects.filter(category=category)  # Assuming Book is a Django model

    # Assertions
    assert books_in_category.exists()  # Ensure that at least one book is found in the category
    for book in books_in_category:
        assert book.category == category  # Check if the category matches for each book
