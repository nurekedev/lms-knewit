from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator


def home_page(request):
    courses = models.Course.published.all()
    return render(request, 'course/home.html', {"courses": courses})


def enrollment_page(request):
    enrlmnt = models.Enrollment.objects.filter(student=request.user)
    context = {"user_courses": enrlmnt}
    return render(request, 'course/enrollment.html', context=context)


def course_detail(request, day, month, year, course_data):
    course_data = get_object_or_404(models.Course,
                                    status=models.Course.Status.PUBLISHED,
                                    slug=course_data,
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day,
                                    )

    if request.user.is_authenticated:
        enrolled_student = models.Enrollment.objects.filter(student=request.user, course=course_data).first()

        if enrolled_student:
            modules_for_course = course_data.module.all()
            materials_for_course = models.Material.objects.filter(module__in=modules_for_course)
            paginator = Paginator(materials_for_course, 2)
            page_number = request.GET.get('page', 1)
            materials_for_course = paginator.page(page_number)

            return render(request, 'course/detail.html',
                          {"course_data": course_data, "modules_for_course": modules_for_course,
                           "materials_for_course": materials_for_course})
        else:
            return render(request, 'course/course_info.html', {"course_data": course_data})
    else:
        return render(request, 'course/course_info.html', {"course_data": course_data})


def about(request):
    return HttpResponse('<h1>О нас</h2>')

def contact(request):
    return HttpResponse('<h1>Контакты</h2>')
