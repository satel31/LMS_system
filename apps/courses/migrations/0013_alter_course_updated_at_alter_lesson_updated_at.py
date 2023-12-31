# Generated by Django 4.2.3 on 2023-07-31 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_course_updated_at_lesson_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время обновления'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время обновления'),
        ),
    ]
