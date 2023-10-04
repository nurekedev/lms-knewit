from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def home_page(request):
    courses = models.Course.published.all()
    return render(request, 'course/home.html', {"courses": courses})


def course_detail(requset, day, month, year, course_data):
    course_data = get_object_or_404(models.Course,
                                    status=models.Course.Status.PUBLISHED,
                                    slug=course_data,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day,
                                    )

    modules_for_course = course_data.module.all()
    materials_for_course = models.Material.objects.filter(module__in=course_data.module.all())

    return render(requset, 'course/detail.html',
                  {"course_data": course_data,
                   "weeks_for_course": modules_for_course,
                   "materials_for_course": materials_for_course})


def about(request):
    return HttpResponse('<h1>О нас</h2>')


def contact(request):
    return HttpResponse('<h1>Контакты</h2>')