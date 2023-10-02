from django.contrib import admin
from django.urls import path, include
from school.views import StudentsViewSet, CourseViewSet, RegistrationViewSet, ListStudentRegistration, EnrolledStudentsList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('registrations', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('students/<int:pk>/registrations/', ListStudentRegistration.as_view()),
    path('course/<int:pk>/registrations/', EnrolledStudentsList.as_view()),
]
