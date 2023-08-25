from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
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
class Course(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    image = models.ImageField(upload_to='images')
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    published = PublishedManager()

    def __str__(self):
        return f"{self.course_name} - {self.category}"

    def calculate_user_progress(self, user):
        total_weeks = Week.objects.filter(course=self).count()
        completed_weeks = CourseWeek.objects.filter(course=self, user=user, status=True).count()
        progress_percentage = (completed_weeks / total_weeks) * 100 if total_weeks > 0 else 0
        return progress_percentage

    def get_absolute_url(self):
        return reverse('course:detailed_info', args=[self.publish.day,
                                                     self.publish.month,
                                                     self.publish.year,
                                                     self.slug])




class Week(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.week_name} - {self.course}"

class CourseWeek(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class Material(models.Model):
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    material_title = models.CharField(max_length=200)
    body_text = models.TextField()
    video_url = models.URLField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material_title


class CourseUser(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



# Draft
# class UserCourseProgress(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course_detail = models.ForeignKey(CourseDetail, on_delete=models.CASCADE)
#
#     def calculate_progress(self):
#         total_videos = Video.objects.filter(course_detail=self.course_detail).count()
#         viewed_videos = self.videoprogress_set.filter(viewed=True).count()
#         return (viewed_videos / total_videos) * 100 if total_videos > 0 else 0
#
#     def __str__(self):
#         return f"{self.user.username} - {self.course_detail.course.course_name}"
#
# class VideoProgress(models.Model):
#     user_course_progress = models.ForeignKey(UserCourseProgress, on_delete=models.CASCADE)
#     video = models.ForeignKey(Video, on_delete=models.CASCADE)
#     viewed = models.BooleanField(default=False)
#
#     class Meta:
#         unique_together = ('user_course_progress', 'video')
#
#     def __str__(self):
#         status = "Viewed" if self.viewed else "Not Viewed"
#         return f"{self.user_course_progress.user.username} - {self.user_course_progress.course_detail.course.course_name} - {self.video.title} - {status}"
#

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset()\
#                       .filter(status=CourseDetail.Status.PUBLISHED)
#

# class Course(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class CourseDetail(models.Model):
#
#     class Status(models.TextChoices):
#         DRAFT = 'DF', 'Draft'
#         PUBLISHED = 'PB', 'Published'
#
#     more_text = models.TextField()
#     status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     published = PublishedManager()
#
#     def __str__(self):
#         return f"{self.course.name} - {self.more_text}"
#
#
# class YouTubeLink(models.Model):
#     course_detail = models.ForeignKey(CourseDetail, on_delete=models.CASCADE)
#     link = models.URLField()
#
#     def __str__(self):
#         return self.link
#
#
# class UserCourseDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     course_detail = models.ForeignKey(CourseDetail, on_delete=models.CASCADE)
#     enrollment_date = models.DateTimeField(default=timezone.now())
#
#     def __str__(self):
#         return f"{self.enrollment_date}"
#
