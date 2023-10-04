from django import forms
from .models import Course, Category, Teachers, Week, Student, Enrollment, Material


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class TeachersForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = '__all__'


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'


class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
