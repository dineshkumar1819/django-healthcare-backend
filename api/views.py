from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Patient, Doctor, PatientDoctor
from .serializers import *

# User registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# View to list and create patients associated with the logged-in user
class PatientView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Return patients for the authenticated user only
    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    # Automatically associate new patient with logged-in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# View to retrieve, update, or delete a specific patient
class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to list and create doctors
class DoctorView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to retrieve, update, or delete a specific doctor
class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to map patients with doctors (create and list mappings)
class MappingView(generics.ListCreateAPIView):
    queryset = PatientDoctor.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

# View to retrieve doctor-patient mapping for a specific patient ID
class PatientDoctorList(generics.RetrieveAPIView):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Get all mappings for a given patient
    def get_queryset(self):
        return PatientDoctor.objects.filter(patient__id=self.kwargs['pk'])
