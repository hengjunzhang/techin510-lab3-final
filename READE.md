# Task Management App

## Project Overview
This project is a task management application built with Streamlit and SQLite. It allows users to add, update, delete, and list tasks with attributes such as name, description, state, created at, created by, and category. This application aims to demonstrate the integration of a simple database with a Streamlit interface for effective task management.

## Features
- **Task Addition:** Users can add tasks with detailed information.
- **Task Listing:** Displays all tasks with options to search by name or description and filter by category.
- **Task State Update:** Allows marking tasks as done.
- **Task Deletion:** Users can delete tasks.

## Learnings
- Gained hands-on experience with Streamlit and SQLite, understanding how to integrate a database into a Streamlit app.
- Learned about the `pydantic` library for data validation and settings management using Python type annotations.
- Explored Python's `datetime` and `enum` modules to handle date/time information and to define a custom enumeration, respectively.

## Reflections
- The initial version of the code lacked modularity, making it somewhat challenging to maintain and update. Refactoring the code into smaller functions significantly improved readability.
- Realized the importance of Streamlit components in enhancing user interaction. Initially, only basic components were used, but later, more complex elements like forms and sidebar filters were incorporated.
- Encountered challenges in efficiently querying the SQLite database, especially in implementing search and filter functionalities. Overcoming these challenges was a valuable learning experience.

## Questions
- What are best practices for structuring a Streamlit app to make it scalable and maintainable?
- How can we optimize SQLite queries for performance in a Streamlit app?
- Are there advanced Streamlit features or components that could further improve the app's functionality and user experience?

## Code Improvements
- **Code Readability and Style:** Improved by adhering to PEP 8 guidelines, adding comments, and using descriptive variable names.
- **Modularity:** Refactored the app into smaller, more manageable functions that handle specific aspects of the app's functionality (e.g., `create_table`, `insert_task`, `list_tasks`).
- **Streamlit Components Usage:** Enhanced the app's interactivity by incorporating more Streamlit components like `st.sidebar` for filtering tasks, `st.expander` for detailed task views, and using `st.form` for submitting new tasks.

## Future Enhancements
- Plan to introduce user authentication to allow multiple users to manage their tasks securely.
- Considering adding a feature for task deadlines with notifications for upcoming due dates.
- Exploring the possibility of deploying the app for wider accessibility.

## Running the App
To run this Streamlit app, ensure you have Streamlit and SQLite installed, then navigate to the project directory and execute:
