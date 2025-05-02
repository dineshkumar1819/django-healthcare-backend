from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # User registration and login
    path('auth/register/', views.RegisterView.as_view()),         # Endpoint to register a new user
    path('auth/login/', TokenObtainPairView.as_view()),           # JWT-based login to get access and refresh tokens

    # Patient endpoints
    path('patients/', views.PatientView.as_view()),               # List all patients (for the logged-in user) or create new
    path('patients/<int:pk>/', views.PatientDetailView.as_view()),# Retrieve, update, or delete a patient by ID

    # Doctor endpoints
    path('doctors/', views.DoctorView.as_view()),                 # List or create doctors
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view()),  # Retrieve, update, or delete a doctor by ID

    # Mapping patients to doctors
    path('mappings/', views.MappingView.as_view()),               # List or create patient-doctor mappings
    path('mappings/<int:pk>/', views.PatientDoctorList.as_view()) # Retrieve mappings for a specific patient by patient ID
]
