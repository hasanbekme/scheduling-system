from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, StudentViewSet, TutorViewSet, AvailabilityViewSet

router = DefaultRouter()
router.register(r'availability', AvailabilityViewSet, basename='availability')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'tutors', TutorViewSet, basename='tutor')


urlpatterns = [
    path('', include(router.urls)),
]