# pydantic-bookstore
We are developing a "Bookstore" API using the FastAPI framework, which will enable users to perform basic CRUD (Create, Read, Update, Delete) operations. This API allows users to add, retrieve, update, and delete books from a virtual bookstore.

Step 1 : Install libraries

To create an API using FastAPI, install both FastAPI and Uvicorn. FastAPI is used for building the API, and Uvicorn is used to run the server. Therefore, it is necessary to install both of these libraries on your system.

pip install fastapi
pip install uvicorn
Step 2: Python code

The code defines endpoints for creating, retrieving, updating, and deleting books. Below is an explanation of the code:

1) Import necessary libraries

FastAPI is imported from the fastapi library for creating the web application.
HTTPException is imported from fastapi for handling HTTP exceptions.
BaseModel is imported from pydantic to create a Pydantic model for book data.
List is imported from the typing module to specify that some endpoints return lists of books.
2) Create a FastAPI application instance

app is an instance of FastAPI used to define routes and handlers for the web application.
3)Define a Pydantic model for books:

The Book class is created, inheriting from BaseModel, and it defines the expected structure of book data.
It has four fields: title, author, publication_year, and ISBN, each with their respective data types.
4) Initialize an empty list to store book data

books is an empty list used to store book objects.
5) Define various endpoints for the API

/books/ (POST): Used to create a new book. The create_book function is responsible for processing this request. It expects a Book object as input, appends it to the books list, and returns the created book.
/books/ (GET): Retrieves a list of all books using the get_books function, returning a list of books.
/books/{ISBN} (GET): Retrieves a specific book by its ISBN. The get_book function searches for a book with the provided ISBN and returns it. If not found, it raises an HTTP 404 error.
/books/{ISBN} (PUT): Updates a book with a specific ISBN. The update_book function finds the book by ISBN, updates its details with the provided data, and returns the updated book. If not found, it raises an HTTP 404 error.
/books/{ISBN} (DELETE): Deletes a book by ISBN. The delete_book function removes the book from the books list and returns the deleted book. If not found, it raises an HTTP 404 error.
6) Run the FastAPI application

The if __name__ == "__main__": block checks if the script is being run as the main program. If so, it imports uvicorn and runs the FastAPI application on the specified host and port (127.0.0.1:8000).
