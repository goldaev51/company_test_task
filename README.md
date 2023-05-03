# company_test_task

## Task Description

Task: Creating a web application for managing a task list<br>
The goal is to create a Django web application for managing a task list. The application should contain the following pages:<br>

1. Main page with a list of all tasks, sorted by creation date. On this page, task titles and creation dates should be displayed. Users should be able to navigate to the task page to view full information.
2. Task page, displaying full information about the task, including the title, description, creation date, and status (completed or not). Users should be able to change the task status.
3. Page for creating a new task, where users can enter a title, description, and due date for the task.
4. Task editing page, where users can change the title, description, and due date of the task.
5. Authorization page for access to task creation, editing, and deletion pages. Access to these pages should be restricted to authorized users only.

--------

## Launch
* clone current repository
* create local venv
* pip install -r requirements.txt
* python manage.py makemigrations
* python manage.py migrate
* ./manage.py create_test_tasks 20
* ./manage.py runserver

