from django.db import models
from django.contrib.auth.models import User

# Model to store patient details
class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each patient to a specific user (owner)
    name = models.CharField(max_length=100)                   # Patient's name
    age = models.IntegerField()                               # Patient's age
    address = models.TextField()                              # Patient's address

# Model to store doctor details
class Doctor(models.Model):
    name = models.CharField(max_length=100)                   # Doctor's name
    specialization = models.CharField(max_length=100)        # Field of specialization (e.g., cardiologist)

# Model to map patients to doctors (many-to-many relationship using intermediate model)
class PatientDoctor(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Reference to patient
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)    # Reference to doctor
