from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('auth/register/', views.RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('patients/', views.PatientView.as_view()),
    path('patients/<int:pk>/', views.PatientDetailView.as_view()),
    path('doctors/', views.DoctorView.as_view()),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view()),
    path('mappings/', views.MappingView.as_view()),
    path('mappings/<int:pk>/', views.PatientDoctorList.as_view()),
]
