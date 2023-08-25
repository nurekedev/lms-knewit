from django import forms
from .models import Category, Course, Week, CourseWeek, Material, CourseUser

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['category', 'course_name', 'slug', 'publish', 'status']

class WeekForm(forms.ModelForm):
    class Meta:
        model = Week
        fields = ['course', 'week_name']

class CourseWeekForm(forms.ModelForm):
    class Meta:
        model = CourseWeek
        fields = ['course', 'week', 'status']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['week', 'material_title', 'body_text', 'video_url', 'publish']

class CourseUserForm(forms.ModelForm):
    class Meta:
        model = CourseUser
        fields = ['category', 'course', 'user']

class TeachersForm(forms.ModelForm):
    class Meta:
        fields: '__all__'


