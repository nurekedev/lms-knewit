# Generated by Django 4.2.4 on 2023-09-29 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 14, 31, 32, 363326, tzinfo=datetime.timezone.utc)),
        ),
    ]
