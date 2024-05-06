from django.urls import include, path
from rest_framework import routers
from .views import DoctorViewSet, PatientViewSet, AppointmentViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]