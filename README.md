# 📰 Daily-News API

**Daily-News** is a RESTful API built with Django REST Framework for managing and publishing articles, handling user ratings, author and category management, and image uploads using Cloudinary. It features token-based authentication, permission handling, and automatically generated Swagger documentation.

---

## 🚀 Features

- ✅ JWT-based authentication with [Djoser](https://djoser.readthedocs.io/)
- 📝 Article CRUD with category and author relations
- 📁 Upload and serve article images via Cloudinary
- ⭐ User ratings on articles (0 to 4 scale)
- 🔐 Admin and authenticated user access control
- 📚 Filterable, paginated endpoints with Django Filter
- 🌐 Interactive API docs with Swagger UI (DRF-YASG)

---

## 🏗️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- Djoser (User Management & Authentication)
- DRF-YASG (Swagger API Docs)
- Django Filters
- Cloudinary (for image uploads)
- Whitenoise (for static file handling in production)

---

## 📂 App Structure

| App      | Description                                      |
|----------|--------------------------------------------------|
| `users`  | Custom user model and authentication             |
| `article`| Models and views for articles, authors, ratings  |
| `api`    | ViewSets, serializers, and URL routing           |

---

## 🧩 Models Overview

### Category
```python
name: CharField
descriptions: TextField
````

### Author

```python
name: CharField
biography: TextField
```

### Article

```python
headline: CharField
body: TextField
category: FK(Category)
author: FK(Author)
publishing_date: DateTimeField
```

### ArticleImage

```python
article: FK(Article)
image: CloudinaryField
```

### Ratings

```python
user: FK(User)
article: FK(Article)
value: IntegerField (0 to 4)
```

---

## 📦 Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Mehedi-Hasan-18/Daily-News.git
cd Daily-News
```

2. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

---

## 🔐 API Authentication

This project uses JWT tokens via Djoser.

* Obtain token:

```
POST /auth/jwt/create/
```

* Refresh token:

```
POST /auth/jwt/refresh/
```

* Endpoints for registration, password reset, etc., are provided via Djoser.

---

## 📘 API Documentation

Visit the auto-generated Swagger UI:

```
http://localhost:8000/swagger/
```

Or the ReDoc alternative:

```
http://localhost:8000/redoc/
```

---

## 🧪 Example Endpoints

| Method | Endpoint                      | Description                       |
| ------ | ----------------------------- | --------------------------------- |
| GET    | `/api/v1/articles/`              | List all articles                 |
| POST   | `/api/v1/articles/`              | Create a new article (admin only) |
| GET    | `/api/v1/categories/`            | List all categories               |
| GET    | `/api/v1/authors/`               | List all authors                  |
| POST   | `/api/v1/articles/{id}/ratings/` | Rate an article (auth users only) |

---

## ⚙️ Deployment Notes

* Ensure you configure **Cloudinary** for image handling in production.
* Use **Whitenoise** for static file support.
* Add environment variables for secret keys and database credentials.

---

## 📄 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

## 🙋‍♂️ Author

**Mehedi Hasan**
🔗 [GitHub Profile](https://github.com/Mehedi-Hasan-18)

---
