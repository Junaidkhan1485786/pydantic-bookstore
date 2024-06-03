# We will create a project for a simple “Bookstore” API.
# This API will enable users to perform basic CRUD (Create, Read, Update, Delete) operations,
# allowing them to add, retrieve, update, and delete books from a virtual bookstore.
# To represent book data, we define a Pydantic model called “Book,” which includes attributes
# like title, author, publication year, and ISBN.
# Pydantic models are used for data validation and serialization.
# The project’s goal is to provide users with essential functionality, including adding new books,
# retrieving a list of all books, fetching a specific book by its unique ISBN, updating book details,
# and deleting books from the collection. We will develop this project using the FastAPI framework,
# offering a practical demonstration of how to build a RESTful API with CRUD functionality.



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create a FastAPI application instance
app = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    publication_year: int
    ISBN: int

# Initialize an empty list to store book data
books = []


# Create a book - POST request


@app.post("/books/", response_model=Book)
async def create_book(book: Book):
    # Add the provided book to the list of books
    books.append(book)
    # Return the created book as the response
    return book


# Get all books - GET request


@app.get("/books/", response_model=List[Book])
async def get_books():
    return books  # Return the list of books as the response


# Get a specific book by ISBN - GET request


@app.get("/books/{ISBN}", response_model=Book)
async def get_book(ISBN: int):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")
    return book  # Return the found book as the response


# Update a book by ISBN - PUT request


@app.put("/books/{ISBN}", response_model=Book)
async def update_book(ISBN: int, updated_book: Book):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")

    # Update book details with the provided data
    for field in updated_book.dict(exclude_unset=True):
        setattr(book, field, getattr(updated_book, field))
    return book  # Return the updated book as the response


# Delete a book by ISBN - DELETE request


@app.delete("/books/{ISBN}", response_model=Book)
async def delete_book(ISBN: int):
    # Search for the book with the specified ISBN
    book = next((b for b in books if b.ISBN == ISBN), None)
    if book is None:
        # If book is not found, raise an HTTP 404 error
        raise HTTPException(status_code=404, detail="Book not found")

    # Remove the book from the list of books
    books.remove(book)
    return book  # Return the deleted book as the response

