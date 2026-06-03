# Backend API Development - Student Management API

<img width="970" height="658" alt="Screenshot 2026-06-04 005136" src="https://github.com/user-attachments/assets/be41ddf3-137c-4d1e-b06c-b83a0196e332" />

## Project Overview

This project is a simple Backend API Development project built using Django and Django REST Framework (DRF).

The project demonstrates the fundamentals of backend development, API creation, request handling, validation, JSON responses, and database integration.

The API allows users to:

* View student records
* Add new students
* Validate user input
* Return proper JSON responses
* Use appropriate HTTP status codes

---

## Technologies Used

* Python
* Django
* Django REST Framework (DRF)
* MySQL / SQLite
* Thunder Client
* JSON

---

## Project Features

### GET API

Retrieve all student records.

Example:

GET /student/

Response:

```json
[
    {
        "id": 1,
        "name": "Mithra",
        "email": "mithra@gmail.com"
    }
]
```

---

### POST API

Add a new student.

Example:

POST /student/

Request Body:

```json
{
    "name": "Mithra",
    "email": "mithra@gmail.com"
}
```

Response:

```json
{
    "message": "Student added successfully"
}
```

---

## Validation

The API validates:

* Name field is required
* Email field is required
* Invalid requests return error messages

Example:

```json
{
    "message": "All fields required"
}
```

Status Code:

```http
400 Bad Request
```

---

## HTTP Status Codes Used

| Status Code | Meaning     |
| ----------- | ----------- |
| 200         | OK          |
| 201         | Created     |
| 400         | Bad Request |

---

## Project Implementations

### 1. Django JsonResponse API

Implemented using:

* JsonResponse
* Python Lists
* Request Body Parsing
* Manual Validation

Features:

* GET API
* POST API
* JSON Response
* Status Codes

---

### 2. Django REST Framework API
<img width="1067" height="670" alt="Screenshot 2026-06-04 005407" src="https://github.com/user-attachments/assets/bf429425-917f-44b0-bc22-adf49c488116" />


Implemented using:

* Model
* Serializer
* API View
* Database Storage

Features:

* GET API
* POST API
* Data Validation
* Database Integration
* Serializer Support

---

## Database Model

Student Model:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

---

## API Testing

The APIs were tested using:

* Thunder Client
* Django REST Framework Browser API

---

## Learning Outcomes

Through this project, I learned:

* Backend Development Fundamentals
* API Development
* Request and Response Handling
* JSON Data Processing
* Input Validation
* HTTP Status Codes
* Django REST Framework
* Database Operations
* API Testing

---

## Future Improvements

* PUT API (Update Student)
* DELETE API (Delete Student)
* Authentication & Authorization
* JWT Authentication
* Pagination
* Search & Filtering

---

## Author

Mithra Tarvin

Diploma in Computer Science Engineering

GitHub: https://github.com/Nikhat2325
