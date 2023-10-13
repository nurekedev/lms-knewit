from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset() \
            .filter(status=Course.Status.PUBLISHED)


class Category(models.Model):
    title = models.CharField(max_length=100)
    descriptiion = models.TextField()

    def __str__(self):
        return self.title


class Teachers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Material(models.Model):
    class MaterialType(models.TextChoices):
        VIDEO_LINK = 'VIDEO', 'Video'
        LECTURE = 'LECTURE', 'Lecture'

    material_title = models.CharField(max_length=200)
    material_type = models.CharField(max_length=10, choices=MaterialType.choices, default=MaterialType.VIDEO_LINK)
    body_text = models.TextField()
    video_url = models.URLField(blank=True)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_title


class Module(models.Model):
    module_name = models.CharField(max_length=255)
    module_description = models.TextField()
    materials = models.ManyToManyField(Material)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return f"{self.module_name} - {self.module_description}"


class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='images')

    preview_image = models.ImageField(upload_to='images')
    about_course = models.TextField()

    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    module = models.ManyToManyField(Module)

    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def calculate_max_score(self):
        total_max_score = 0
        for module in self.module.all():
            total_max_score += (module.materials.filter(material_type=Material.MaterialType.VIDEO_LINK).count() * 3)
            total_max_score += (module.materials.filter(material_type=Material.MaterialType.LECTURE).count() * 2)
        self.max_score = total_max_score
        self.save()
        return self.max_score

    def get_absolute_url(self):
        return reverse('course:detailed_info', args=[self.publish.day,
                                                     self.publish.month,
                                                     self.publish.year,
                                                     self.slug])

    def __str__(self):
        return f"{self.course_name} - {self.category}"


class Enrollment(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    mark = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.student} | {self.course} | {self.enrollment_date} | {self.mark}"


class Progress(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed_videos = models.PositiveIntegerField(default=0)
    completed_lectures = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Progress for {self.enrollment.course.course_name}"
