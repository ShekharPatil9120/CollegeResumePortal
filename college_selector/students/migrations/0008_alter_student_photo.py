# Generated by Django 5.1.3 on 2024-12-01 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, default='students/default_photo.png', null=True, upload_to='students/'),
        ),
    ]
