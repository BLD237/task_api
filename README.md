# Task App API

Task App API is a RESTful API for task management built with **FastAPI** and **MySQL**.  
It supports full CRUD operations on tasks and categories with user authentication via OAuth2.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Data Models](#data-models)
- [Example Requests](#example-requests)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- User registration and login with JWT token authentication  
- Create, read, update, and delete tasks  
- Create, read, update, and delete categories  
- Task attributes include title, description, category, priority, due date/time, and status  
- Secure API endpoints protected with OAuth2 password flow  

---

## Tech Stack

- **Backend:** FastAPI  
- **Database:** MySQL  
- **Authentication:** OAuth2 password flow (JWT tokens)  
- **ORM:** SQLAlchemy 

---

## Getting Started

### Prerequisites

- Python 3.9+  
- MySQL server  
- `pip` package manager  

### Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/yourusername/task-app-api.git
   cd task-app-api
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your MySQL database connection in `.env` or settings file:

   ```env
   DATABASE_URL=mysql+pymysql://username:password@localhost:3306/taskappdb
   ```

5. Run database migrations (if applicable):

   ```bash
   alembic upgrade head
   ```

6. Start the server:

   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Authentication

| Endpoint               | Method | Description          |
|------------------------|--------|----------------------|
| `/api/auth/register`   | POST   | Register a new user  |
| `/api/auth/login`      | POST   | Login and get token  |

### Tasks (Authentication required)

| Endpoint                  | Method | Description             |
|---------------------------|--------|-------------------------|
| `/api/tasks`              | GET    | Get all tasks           |
| `/api/tasks`              | POST   | Create a new task       |
| `/api/tasks/{task_id}`    | GET    | Get a task by ID        |
| `/api/tasks/{task_id}`    | PUT    | Update a task by ID     |
| `/api/tasks/{task_id}`    | DELETE | Delete a task by ID     |

### Categories (Authentication required)

| Endpoint                     | Method | Description              |
|------------------------------|--------|--------------------------|
| `/api/categories/`           | GET    | Get all categories       |
| `/api/categories/`           | POST   | Create a new category    |
| `/api/categories/{category_id}` | PUT    | Update a category by ID  |
| `/api/categories/{category_id}` | DELETE | Delete a category by ID  |

---

## Authentication

- Use `/api/auth/login` to authenticate with your email and password.
- Receive an access token (JWT) in response.
- Include the token in requests to protected endpoints:

```
Authorization: Bearer <access_token>
```

---

## Data Models

### UserCreate

```json
{
  "name": "string",
  "email": "string",
  "password": "string"
}
```

### LoginUser

```json
{
  "email": "string",
  "password": "string"
}
```

### TaskCreateModel

```json
{
  "title": "string",
  "description": "string",
  "category": "string",
  "priority": "string",
  "due_date": "YYYY-MM-DDTHH:MM:SSZ",
  "due_time": "HH:MM:SS",
  "status": "string"
}
```

### CategoryCreate

```json
{
  "title": "string",
  "description": "string"
}
```

---

## Example Requests

### Register a User

```bash
curl -X POST "http://localhost:8000/api/auth/register" \
-H "Content-Type: application/json" \
-d '{"name":"John Doe","email":"john@example.com","password":"password123"}'
```

### Login

```bash
curl -X POST "http://localhost:8000/api/auth/login" \
-H "Content-Type: application/json" \
-d '{"email":"john@example.com","password":"password123"}'
```

### Create a Task

```bash
curl -X POST "http://localhost:8000/api/tasks" \
-H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
  "title": "Finish Report",
  "description": "Complete the financial report",
  "category": "Work",
  "priority": "High",
  "due_date": "2025-08-20T00:00:00Z",
  "due_time": "17:00:00",
  "status": "Pending"
}'
```

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.

---

**Happy task managing!**
