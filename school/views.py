from rest_framework import viewsets, generics
from school.models import Student, Course, Registration
from school.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer, ListStudentRegistrationSerializer, EnrolledStudentsListSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """Exibe todos os alunos"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistrationViewSet(viewsets.ModelViewSet):
    """Exibe todas as matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListStudentRegistration(generics.ListAPIView):
    """Listando as matrículas de um aluno"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentRegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrolledStudentsList(generics.ListAPIView):
    """Listando alunos matriculados em um curso"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = EnrolledStudentsListSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]