# Expense Management System

This is a Django-based application for managing users and expenses, with automatic bill splitting based on selected methods.

## Prerequisites

- Python 3.x
- Django
- Django REST Framework

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/deepak982/Daily-Expenses-Sharing-Application.git
    cd expenses
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. **Make migrations:**

    ```bash
    python manage.py makemigrations
    ```

2. **Migrate:**

    ```bash
    python manage.py migrate
    ```

## Static Files

1. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

## Running the Server

1. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Users

- **List all users:**

    ```http
    GET /api/users/
    ```

- **Retrieve a specific user:**

    ```http
    GET /api/users/{id}/
    ```

- **Create a new user:**

    ```http
    POST /api/users/
    
    {
        "email": "user@example.com",
        "name": "User Name",
        "mobile": "1234567890"
    }
    ```

### Expenses

- **List all expenses:**

    ```http
    GET /api/expenses/
    ```

- **Retrieve a specific expense:**

    ```http
    GET /api/expenses/{id}/
    ```

- **Create a new expense with automatic bill splitting:**

    ```http
    POST /api/expenses/
    
    {
        "description": "Dinner at Restaurant",
        "total_amount": 100.0,
        "split_method": "equal",  # Options: "equal", "exact", "percentage"
        "user": 1,  # User ID who paid the expense
        "participants": {
            "2": 0,
            "3": 0
        }
    }
    ```

    **Note:** The `participants` field should contain user IDs with initial amounts set to `0`. The system will automatically calculate the amounts based on the selected `split_method`.

## Example JSON Data

### Create User

```json
{
    "email": "user1@example.com",
    "name": "User One",
    "mobile": "1234567890"
}

Create Expense with Equal Split

{
    "description": "Lunch",
    "total_amount": 60.0,
    "split_method": "equal",
    "user": 1,
    "participants": {
        "2": 0,
        "3": 0
    }
}


Create Expense with Exact Split

{
    "description": "Movie Tickets",
    "total_amount": 30.0,
    "split_method": "exact",
    "user": 1,
    "participants": {
        "2": 10,
        "3": 20
    }
}

Create Expense with Percentage Split

{
    "description": "Grocery Shopping",
    "total_amount": 100.0,
    "split_method": "percentage",
    "user": 1,
    "participants": {
        "2": 50,
        "3": 50
    }
}


### Key Points

- **Split Method and Participants:** Users enter `participants` with initial amounts set to `0`, and the system automatically calculates the amounts based on the selected `split_method`.
- **Endpoints:** Users can create, retrieve, and list users and expenses through the provided API endpoints.

### Dependencies File

Ensure you have a `requirements.txt` file with the necessary dependencies:

```txt
Django>=3.0,<4.0
djangorestframework>=3.11

