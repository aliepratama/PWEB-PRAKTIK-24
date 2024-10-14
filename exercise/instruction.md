### Student Exercise: Book Management Web Application

#### Objective:
The purpose of this exercise is to familiarize students with basic web development using Flask, a popular micro-framework for Python. Students will learn how to handle CRUD (Create, Read, Update, Delete) operations using a simple data structure (list of dictionaries) to manage data. This project will also introduce students to HTML templating with Jinja2, which Flask supports natively, allowing them to understand the basics of server-side data rendering and template inheritance.

#### Project Overview:
You will develop a simple book management web application that allows users to add, view, update, and delete book records. This app will use Flask for the backend, HTML for the frontend, and a list of dictionaries in Python to simulate a database.

#### Requirements:
1. **Flask Setup:**
   - Install Flask.
   - Create a basic Flask application structure.

2. **Data Structure:**
   - Define a list of dictionaries to store book data. Each dictionary represents a book with attributes like `id`, `title`, `author`.

3. **HTML Templates:**
   - Use Jinja2 template inheritance to create a base template (`base.html`) which includes common elements like the document structure, a header, and a footer.
   - Create other templates such as `index.html` for showing all books, `add_book.html` for adding a new book, and `edit_book.html` for editing an existing book. These templates should inherit from the base template.

4. **CRUD Operations:**
   - **Create:** Build a form to submit new book details. When the form is submitted, a new dictionary should be added to the list.
   - **Read:** Display all books from the list on the `index.html` page, with options to edit or delete each book.
   - **Update:** Each book entry should have an 'Edit' button that loads the book details into a form where they can be modified.
   - **Delete:** Next to each book, include a 'Delete' button that will remove the book from the list.

5. **Routing:**
   - Set up Flask routes to handle different parts of the app. For example, `/` for the home page, `/add` for the add book form, `/edit/<id>` for the edit form, and `/delete/<id>` for deleting a book.

6. **Template Inheritance:**
   - Implement Jinja2 template inheritance to reuse the layout defined in `base.html` across all other templates. This minimizes code redundancy and enhances maintainability.

#### Deliverables:
- A fully functional Flask application that meets the above requirements.
- Use of template inheritance to manage HTML content efficiently.
- Implementation of CRUD operations using a list of dictionaries as the data store.

#### Evaluation Criteria:
- Functionality: All features (CRUD operations) should work as specified.
- Code Quality: Code should be clean, well-commented, and easy to read.
- Use of Template Inheritance: Proper use of Jinja2 template inheritance should be demonstrated.

#### Tips:
- Test each feature thoroughly before moving on to the next.
- Regularly commit your code to a version control system to keep track of changes and ensure data is not lost.
- Refer to Flask and Jinja2 documentation for additional help and best practices.

This exercise encourages practical application of web development concepts and Python programming, which are essential skills for aspiring software developers.