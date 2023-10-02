from rest_framework import serializers
from school.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
            'rg',
            'cpf',
            'date_of_birth',
        ]

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            'id',
            'code',
            'name',
            'category',
            'description',
            'level',
        ]

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = [
            'id',
            'student',
            'course',
            'period',
        ]

class ListStudentRegistrationSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.name')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'period']

    def get_period(self, obj):
        return obj.get_period_display()
    
class EnrolledStudentsListSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']