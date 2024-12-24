from django.db import models


class College(models.Model):
    name = models.CharField(max_length=100, verbose_name="College Name")
    logo = models.ImageField(
        upload_to="colleges/",
        default="colleges/default_logo.png",
        verbose_name="College Logo",
    )  # Use a default image

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200, verbose_name="Student Name")
    introduction = models.TextField(
        blank=True, null=True, verbose_name="Introduction"
    )  # Student introduction
    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True,
        default="students/default_photo.png",
        verbose_name="Student Photo",
    )  # Add a default photo
    college = models.ForeignKey(
        College, on_delete=models.CASCADE, related_name="students", verbose_name="College"
    )
    about = models.TextField(
        blank=True, null=True, verbose_name="About"
    )  # Education info, hobbies, etc.
    skills = models.TextField(
        blank=True, null=True, verbose_name="Skills"
    )  # Skills and certifications
    projects = models.TextField(
        blank=True, null=True, verbose_name="Projects"
    )  # Projects details
    internships = models.TextField(
        blank=True, null=True, verbose_name="Internships"
    )  # Internships info
    achievements = models.TextField(
        blank=True, null=True, verbose_name="Achievements"
    )  # Achievements
    goals = models.TextField(
        blank=True, null=True, verbose_name="Goals"
    )  # Goals

    def __str__(self):
        return self.name
