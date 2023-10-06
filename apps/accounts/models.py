from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from apps.course.models import Course
from .managers import MyUserManager
from PIL import Image


# Create your models here.
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    phone_regex = RegexValidator(regex=r'^((\+7)|8)\d{10}$',
                                 message="Phone number must be entered in the format: '+79999999999' or '89999999999'.", )
    phone_number = models.CharField(validators=[phone_regex], max_length=12, unique=True, null=True)
    courses = models.ManyToManyField(Course, through='course.Enrollment')
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpeg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



