````markdown
# Social Media API

A foundational **Social Media API** built with **Django** and **Django REST Framework (DRF)**.  
This project focuses on building a clean, understandable backend architecture with token-based authentication and a custom user model suitable for social platforms.

---

## 🚀 Features

- Custom user model extending Django’s `AbstractUser`
- Token-based authentication using Django REST Framework
- User registration and login
- Authenticated user profile management
- Followers / following relationship
- Clear separation of concerns across the codebase

---

## 🧱 Tech Stack

- Python
- Django
- Django REST Framework
- Django REST Framework Token Authentication
- SQLite (default database)
- Pillow (image handling)

---

## 📁 Project Structure

```text
social_media_api/
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── apps.py
│
├── social_media_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── manage.py
└── README.md
````

---

## 🧩 Code Architecture Overview

This project follows a clear and intentional separation of responsibilities:

* **models.py** → defines what data exists and how it is stored
* **serializers.py** → controls how data is validated, transformed, and exposed via the API
* **views.py** → defines what happens when a client hits an endpoint
* **urls.py** → maps incoming requests to the correct views
* **tokens** → represent user identity for API access (stateless, not sessions)

This structure makes the codebase easier to reason about, maintain, and extend.

---

## 👤 Custom User Model

A custom user model (`accounts.User`) is used to support social features.

### Additional Fields

* `bio` – short user biography
* `profile_picture` – optional profile image
* `followers` – self-referential relationship for following other users

### Why a Custom User Model?

* Enables social networking features
* Avoids complex migrations later
* Aligns with real-world backend requirements

---

## 🔐 Authentication

Authentication is implemented using **Django REST Framework Token Authentication**.

* Tokens are created when a user registers
* Existing tokens are reused on login
* Tokens must be included in the request header for protected endpoints

### Authorization Header Format

```http
Authorization: Token your_token_here
```

---

## 📡 API Endpoints

### Register User

**POST** `/api/accounts/register/`

```json
{
  "username": "kenny",
  "email": "kenny@example.com",
  "password": "strongpassword123",
  "bio": "Full-stack developer"
}
```

---

### Login User

**POST** `/api/accounts/login/`

```json
{
  "username": "kenny",
  "password": "strongpassword123"
}
```

---

### Get User Profile

**GET** `/api/accounts/profile/`

Requires authentication.

---

### Update User Profile

**PUT** `/api/accounts/profile/`

```json
{
  "bio": "Updated bio text"
}
```

---

## ⚙️ Setup Instructions

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate        # Windows
source venv/bin/activate    # macOS/Linux
```

---

### Install Dependencies

```bash
pip install django djangorestframework djangorestframework-authtoken pillow
```

---

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### Run Development Server

```bash
python manage.py runserver
```

---

## 🧪 Testing

Use **Postman**, **Insomnia**, or similar tools to test the API.

Recommended flow:

1. Register a user
2. Copy the returned token
3. Add the token to the Authorization header
4. Access authenticated endpoints

---

## 🧠 Design Principles

* Explicit separation of concerns
* Stateless authentication using tokens
* Readable, maintainable code
* Built to scale with additional social features

---

## 🔮 Future Enhancements

* Follow / unfollow endpoints
* Posts and comments
* Likes and reactions
* Feed aggregation logic
* Permissions and throttling
* Pagination and filtering

---

## 📜 License

This project is intended for educational and demonstration purposes.


