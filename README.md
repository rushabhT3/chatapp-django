# chatapp-django... Notes Project

```markdown

This is a simple Django project for managing and sharing notes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Django 3.2+

### Installation

1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```
5. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

To run the server, execute the following command in the project directory:

```bash
python manage.py runserver
```

## API Endpoints

The application provides the following API endpoints:

- `POST /login`: Log in to the application.
- `POST /signup`: Sign up for a new account.
- `POST /notes/create`: Create a new note.
- `GET /notes/{id}`: Retrieve a specific note by its ID.
- `POST /notes/share`: Share a note with other users.
- `PUT /notes/{id}`: Update an existing note.
- `GET /notes/version-history/{id}`: Get all the changes associated with a note.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
```
```


