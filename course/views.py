from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.template import RequestContext



# Create your views here.
def index(request):
    courses = models.Course.published.all()
    return render(request, 'course/index.html', {"courses":courses})
#
# def course_detail(requset, course_data):
#
#     course_data = get_object_or_404(models.CourseDetail, slug=course_data, status=models.CourseDetail.Status.PUBLISHED)
#     return render(requset, 'course/detail.html', {"course_data":course_data})
def course_detail(requset, day, month, year, course_data):

    course_data = get_object_or_404(models.Course,
                             status=models.Course.Status.PUBLISHED,
                             slug=course_data,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,)

    return render(requset, 'course/detail.html', {"course_data":course_data})

def about(request):
    return HttpResponse('<h1>О нас</h2>')

def contact(request):
    return HttpResponse('<h1>Контакты</h2>')

