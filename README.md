
# FastAPI Todo & Chat API

This project is a backend API built with FastAPI that supports user registration, login with JWT authentication and  task management (TODO list).

---

## Features

- **User Authentication**  
  Register and login users securely with hashed passwords and JWT tokens.

- **Task Management**  
  Users can fetch their TODO tasks .

- **CORS Enabled**  
  API allows cross-origin requests from any origin.

- **Background Task Scheduling**  
  Placeholder for future notification tasks via APScheduler.

---

## Technologies Used

- FastAPI  
- SQLAlchemy ORM  
- SQLite (or any compatible database)  
- JWT for authentication   
- APScheduler (for background tasks, planned)  
- Python 3.9+

---

## Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/fastapi-todo-chat.git
   cd fastapi-todo-chat
   ```

2. **Create and activate a virtual environment (recommended):**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose apscheduler
   ```

4. **Run the app:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Open your browser at** `http://127.0.0.1:8000`

---

## API Endpoints

### Authentication

- **Register User**

  ```
  POST /api/auth/register
  ```

  Request Body:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "yourpassword"
  }
  ```

  Response:
  ```json
  {
    "status": "success",
    "message": "User created successfully"
  }
  ```

- **Login User**

  ```
  POST /api/auth/login
  ```

  Request Body:
  ```json
  {
    "email": "john@example.com",
    "password": "yourpassword"
  }
  ```

  Response:
  ```json
  {
    "status": "success",
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer",
    "message": "Login Successful"
  }
  ```

---

### Tasks

- **Get User Tasks**

  ```
  GET /api/tasks
  ```

  Requires Bearer token in Authorization header.

  Response:
  ```json
  {
    "status": "success",
    "data": [
      {
        "id": 1,
        "title": "Task title",
        "description": "Task description",
        "completed": false,
        "user_id": "user-id"
      }
    ],
    "message": "Data fetched successfully"
  }
  ```

- **Create, Read, Update, Delete Tasks**

  Endpoints for these actions are present but **not implemented yet**.

---



## Project Structure

```
.
├── main.py               # Main FastAPI app, routes, websocket manager
├── database.py           # DB engine and session setup
├── models.py             # SQLAlchemy models: User, Todo
├── auth.py               # Authentication utilities (hashing, JWT)
├── base.py               # Pydantic schemas (request/response models)
├── requirements.txt      # Python dependencies
└── README.md             # This documentation
```

---

## Future Work

- Complete task CRUD operations  
- Implement notifications with APScheduler  


---

## License

MIT © 2025 BLD237(Mufor Belmond)

---

## Contact

If you have questions or want to contribute, please open an issue or contact me at muforbelmond20@gmail.com.
