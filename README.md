# Django Healthcare API Project

This is a simple **Healthcare Management System** built using **Django** and **Django REST Framework (DRF)** with **JWT authentication** and **PostgreSQL** as the database.

---

## Features

- User Registration and JWT-based Login
- Create, Read, Update, Delete (CRUD) for Patients and Doctors
- Map Doctors to Patients (many-to-many)
- Secure endpoints with JWT
- Tested via Postman

---

## Models

- **User** – Built-in Django user model
- **Patient** – Stores name, age, address; linked to user
- **Doctor** – Stores name and specialization
- **PatientDoctor** – Links patients to doctors

---

## APIs (Use Postman)

### **Authentication**
- `POST /auth/register/` – Register new user  
- `POST /auth/login/` – Get JWT token (login)

### **Patients**
- `GET /patients/` – List all patients of logged-in user  
- `POST /patients/` – Create a new patient  
- `GET /patients/<id>/` – View a patient by ID  
- `PUT /patients/<id>/` – Update a patient  
- `DELETE /patients/<id>/` – Delete a patient  

### **Doctors**
- `GET /doctors/` – List all doctors  
- `POST /doctors/` – Create a doctor  
- `GET /doctors/<id>/` – View a doctor by ID  
- `PUT /doctors/<id>/` – Update a doctor  
- `DELETE /doctors/<id>/` – Delete a doctor  

### **Mappings**
- `POST /mappings/` – Assign a doctor to a patient  
- `GET /mappings/<patient_id>/` – Get all doctors assigned to a patient

---

## Tools Used

- Django
- Django REST Framework
- PostgreSQL
- Postman
- JWT (Simple JWT)

---

## Setup Instructions

```bash
git clone <repo-url>
cd <project-folder>

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Configure PostgreSQL in settings.py
# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start the server
python manage.py runserver
