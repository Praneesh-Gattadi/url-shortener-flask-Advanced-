# 🔗 Advanced URL Shortener Web Application

An **Advanced URL Shortener Web Application** built using **Flask (Python)** that allows users to shorten long URLs, securely log in, and manage their shortened links with a personalized history.

This project was developed as part of a hands-on assignment from **Innomatics Research Labs**.

---

## 📌 Features

- 🔐 User Signup & Login (Authentication using Flask-Login)
- ✂️ Shortens long URLs into compact, shareable links
- 📋 One-click access to shortened URLs
- 👤 User-specific URL history
- ✅ URL format validation
- 🗄️ Database integration using SQLite & SQLAlchemy
- 🎨 Clean and simple UI

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Authentication:** Flask-Login  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Frontend:** HTML, CSS  

---

## 📁 Project Structure

```
url_shortener/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── url_shortener.db
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Praneesh-Gattadi/url-shortener-flask-Advanced-.git
cd url-shortener-flask-Advanced-
```

### 2️⃣ Install Dependencies
```bash
pip install flask flask_sqlalchemy flask_login
```

### 3️⃣ Run the Application
```bash
python app.py
```

### 4️⃣ Open in Browser
```
http://127.0.0.1:5000
```

---

## 🧭 Application Workflow

1. User signs up with a unique username (5–9 characters)
2. User logs in using credentials
3. User enters a valid URL to shorten
4. Application generates a short URL
5. Shortened URLs are saved per user
6. User can view previously shortened URLs
7. Clicking the short URL redirects to the original link

---

## 🔐 Validation Rules

- Username must be **unique**
- Username length: **5 to 9 characters**
- URL must start with `http://` or `https://`

---

## 🎯 Learning Outcomes

- Built a full-stack web application using Flask
- Implemented authentication and session management
- Designed relational database models using ORM
- Handled form validation and user errors
- Understood real-world Flask project structure

---

## 📌 Future Enhancements

- Password hashing for improved security
- Custom URL aliases
- Click analytics for shortened URLs
- Deployment on cloud platforms

---

## 🏫 Acknowledgment

This project was developed as part of training and assignments provided by **Innomatics Research Labs**.

---

## Application GUI

<img width="1212" height="555" alt="Image" src="https://github.com/user-attachments/assets/c83f40b1-8b0f-4630-9669-ca6e2c89ada8" />

<img width="1216" height="553" alt="Image" src="https://github.com/user-attachments/assets/fb757432-5391-4bb6-8d34-f3b9e906f577" />

<img width="1203" height="490" alt="Image" src="https://github.com/user-attachments/assets/c8f161f7-8086-45d3-991d-10a4c617c8c5" />

<img width="1203" height="519" alt="Image" src="https://github.com/user-attachments/assets/254b2d2c-d9de-4676-bb16-a280e3443437" />

---

## 📜 License

This project is for educational purposes only.
