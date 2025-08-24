# 🚀 Django Auth API

A **JWT Authentication API with Email OTP Verification** built using **Django REST Framework**.  
This project provides a complete authentication system with OTP-based verification, password reset, secure JWT login/logout, and interactive API documentation.

---

## ✨ Features

- 🔑 **JWT Authentication** (Access & Refresh tokens)  
- 📧 **Email OTP Verification** during registration & password reset  
- 👤 **Custom User Model** with role field (`user_type`)  
- 🔒 **Secure Login/Logout** with token blacklisting  
- 🔁 **Password Reset Flow** (Request OTP → Verify OTP → Set New Password)  
- 📊 **API Documentation** (Swagger & Redoc at `/api/docs/` and `/api/redoc/`)  
- ⚡ **Rate Limiting** (`20/min` for anonymous, `60/min` for authenticated)  
- 🌍 **CORS Enabled** for frontend integration  
- 🧪 **Unit Tests** for full auth flow  

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework  
- **Authentication**: SimpleJWT  
- **OTP Storage**: Redis  
- **Database**: SQLite (development)  
- **Docs**: drf-spectacular (Swagger & Redoc)  
- **CI/CD**: GitHub Actions  

---

## 📂 Project Structure

```
auth_project/
│── auth_project/        # Project config & settings
│── userauth/            # Authentication app
│   ├── models.py        # Custom User model
│   ├── views.py         # API endpoints
│   ├── serializers.py   # DRF serializers
│   ├── urls.py          # Auth routes
│   ├── utils.py         # OTP utilities
│   └── tests.py         # Unit tests
│── manage.py
│── requirements.txt
│── .env.example
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Devesh1651/django-auth-api.git
cd django-auth-api
```

### 2. Create & activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate   # on Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file (see `.env.example`):

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_DB=0
```

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Start Redis
```bash
redis-server
```

### 7. Start server
```bash
python manage.py runserver
```

Now open:
- Swagger UI → [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)  
- Redoc → [http://127.0.0.1:8000/api/redoc/](http://127.0.0.1:8000/api/redoc/)  

---

## 📬 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/register/`               | Register new user (sends OTP) |
| POST   | `/api/verify-otp/`             | Verify OTP & activate user |
| POST   | `/api/login/`                  | Login (JWT Access + Refresh) |
| POST   | `/api/token/refresh/`          | Refresh access token |
| GET    | `/api/profile/`                | Get logged-in user profile |
| POST   | `/api/logout/`                 | Logout & blacklist refresh token |
| POST   | `/api/password-reset-request/` | Request OTP for password reset |
| POST   | `/api/password-reset-verify-otp/` | Verify reset OTP |
| POST   | `/api/set-new-password/`       | Set a new password |

---

## 🧪 Running Tests

```bash
python manage.py test
```

---

## 🤝 Resume Highlights

- Designed & implemented a **secure authentication system** with OTP-based email verification.  
- Built **Swagger API Docs** for professional API documentation.  
- Integrated **Redis** for fast, secure OTP handling.  
- Added **unit tests** to validate the full auth flow.  
- Configured **GitHub Actions CI** for automated testing on every push.  

---

## 📌 Future Improvements

- Docker setup (Django + Redis)  
- PostgreSQL integration for production  
- Role-based permissions (`user_type`)  
- Deployment on cloud (Heroku/AWS/Render)  

---

👨‍💻 **Author**: Devesh Nahar  
🔗 GitHub: [Devesh1651](https://github.com/Devesh1651)
