# Generated by Django 4.2.5 on 2023-10-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_enrollment_student_alter_course_publish'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='courses',
            field=models.ManyToManyField(through='course.Enrollment', to='course.course'),
        ),
    ]