# Generated by Django 4.2.5 on 2023-10-06 04:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_course_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 6, 4, 23, 30, 546088, tzinfo=datetime.timezone.utc)),
        ),
    ]
