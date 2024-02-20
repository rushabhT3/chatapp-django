# chatapp-django... Notes Project

This is a simple Django project for managing and sharing notes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Django 3.2+

### Installation

1. Clone the repository
2. Navigate to the project directory using ```cd notes_project```

3. Install virtualenv If you haven’t installed virtualenv yet, you can do so using pip:
   ```bash
   pip install virtualenv
   ```

   Create a virtual environment Navigate to your project directory and create a new virtual environment.
   ```bash
   virtualenv venv
   ```

### Windows

4. Activate the virtual environment:
   ```bash
   .\venv\Scripts\activate
   ```

### Unix or MacOS

4. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

In these commands, `venv` is the name of the virtual environment. You can replace `venv` with any name you prefer. Once the virtual environment is activated, you can install the necessary packages in it without affecting your global Python environment. To deactivate the virtual environment, you can simply type `deactivate` in your terminal.

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


