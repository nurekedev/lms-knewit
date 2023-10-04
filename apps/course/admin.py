from django.contrib import admin
from .models import Category, Course, Module, Material, Enrollment, Teachers, Progress

admin.site.register(Category)
admin.site.register(Teachers)
admin.site.register(Module)
admin.site.register(Material)
admin.site.register(Enrollment)
admin.site.register(Progress)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('course_name',)}
    list_display = ('course_name', 'category', 'max_score_display')

    def max_score_display(self, obj):
        return obj.calculate_max_score()

    max_score_display.short_description = 'Max Score'


