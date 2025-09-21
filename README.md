# FastAPI Mini Demo: Task Manager

A minimal demonstration of a Task Manager API using the FastAPI framework. This project features two basic routes:

- **GET /tasks:** Lists all tasks currently in memory.
- **POST /tasks:** Creates a new task and adds it to the in-memory list.

The API uses Pydantic for data validation and `pytest` for testing.

## Project Structure

.
├── main.py # Main FastAPI application with routes and in-memory storage
├── pytest.ini # pytest configuration file
├── tests/ # tests folder
│ └── test_fastapi_tasks.py # Tests for the API endpoints
└── venv/

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/yoftil7/task_manager_faskapi.git
    cd task_manager_faskapi
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    # venv\Scripts\activate   # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Start the FastAPI server with `uvicorn`:
    ```bash
    uvicorn main:app --reload
    ```
2.  The API documentation will be available at `http://127.0.0.1:8000/docs`, where you can test the `POST` and `GET` endpoints.

## Running the Tests

To execute the test suite using `pytest`, run the following command from the root directory:

```bash
pytest

License
This project is licensed under the MIT License.
```
