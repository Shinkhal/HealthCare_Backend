# 🏥 Healthcare Backend – Django REST Framework

A backend system for a healthcare application built with **Django, Django REST Framework (DRF), and JWT Authentication**.  
It provides APIs for **user authentication, patient management, doctor management, and patient-doctor mapping**.

---

## 🚀 Features
- User Registration & Login with JWT Authentication
- Patient CRUD APIs (only accessible by the user who created them)
- Doctor CRUD APIs (accessible to all authenticated users)
- Patient–Doctor Mapping APIs (assign/remove doctors to patients)
- Secure database using **PostgreSQL**
- Environment variable support for sensitive configurations
- Built with Django ORM and REST Framework best practices

---

## 🛠 Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Database:** PostgreSQL
- **Tools:** Postman (API testing)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Shinkhal/HealthCare_Backend.git
cd HealthCare_Backend
````

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # on Windows
source venv/bin/activate  # on macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure PostgreSQL

Create a PostgreSQL database and update your `.env` file:

```
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret
DEBUG=True
```

### 5️⃣ Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

### Authentication

* `POST /api/auth/register/` → Register a new user
* `POST /api/auth/login/` → Login and get JWT token
* `POST /api/auth/refresh/` → Refresh access token

### Patients

* `POST /api/patients/` → Add a patient (authenticated user only)
* `GET /api/patients/` → List patients created by the user
* `GET /api/patients/<id>/` → Get patient details
* `PUT /api/patients/<id>/` → Update patient
* `DELETE /api/patients/<id>/` → Delete patient

### Doctors

* `POST /api/doctors/` → Add a doctor
* `GET /api/doctors/` → List all doctors
* `GET /api/doctors/<id>/` → Get doctor details
* `PUT /api/doctors/<id>/` → Update doctor
* `DELETE /api/doctors/<id>/` → Delete doctor

### Patient–Doctor Mapping

* `POST /api/mappings/` → Assign a doctor to a patient
* `GET /api/mappings/` → List all mappings
* `GET /api/mappings/<patient_id>/` → Get doctors for a patient
* `DELETE /api/mappings/<id>/` → Remove a doctor from a patient

---

## 📌 Notes

* Authentication is required for all Patient and Doctor APIs.
* Use JWT tokens in the header:

```
Authorization: Bearer <access_token>
```

---

## ✅ Expected Outcome

* Users can register & login
* Authenticated users can add and manage patients
* Doctors can be managed and assigned to patients
* Data is stored securely in PostgreSQL
