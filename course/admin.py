from django.contrib import admin
from .models import Category, Course, Week, CourseWeek, Material, CourseUser, Teachers


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'publish', 'status']
    prepopulated_fields = {'slug':['course_name',]}


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['week_name', 'course']


@admin.register(CourseWeek)
class CourseWeekAdmin(admin.ModelAdmin):
    list_display = ['course', 'week', 'status']


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material_title', 'week', 'publish']


@admin.register(CourseUser)
class CourseUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'category']

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
