# Generated by Django 4.2.5 on 2023-10-04 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 4, 9, 34, 1, 897331, tzinfo=datetime.timezone.utc)),
        ),
    ]