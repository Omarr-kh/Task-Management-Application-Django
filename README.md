# Task Management System

## Overview

The **Task Management System** is a simple web application built with Django that allows users to create, update, delete, and manage tasks. It includes features like task status filtering (completed, not completed, all tasks), pagination, and more.

## Features

- **Add Tasks**: Create new tasks with a title and description.
- **Task Status Management**: Mark tasks as completed or not completed.
- **Task Filtering**: Filter tasks based on their status (completed, not completed, or all).
- **Pagination**: View tasks with pagination for easy navigation.
- **Task Deletion**: Remove tasks from the list.
- **Task Update**: Edit existing tasks.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Omarr-kh/Task-Management-Application-Django.git
   cd Task-Management-Application-Django
2. **Install packages:**

    ```bash
    pip install -r requirements.txt
3. **Apply migration**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
4. **Run the development server**

    ```bash
    python manage.py runserver
5. **Open localhost**

    ```bash
    http://127.0.0.1:8000/tasks/

## Usage

- **Add a Task**: Navigate to the task creation page and fill out the form to add a new task.
- **Update a Task**: Click on the Update Task button next to the task to modify its details.
- **Delete a Task**: Click on the Delete Task button to remove a task.
- **Filter Tasks**: Use the status filter to view tasks based on their completion status.
- **Paginate Tasks**: Navigate through pages of tasks if there are many.
