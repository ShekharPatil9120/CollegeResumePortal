from django.contrib import admin
from .models import College, Student

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')  # Display these fields in the list view
    search_fields = ('name',)  # Enable search by college name

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'photo')  # Display these fields in the list view
    list_filter = ('college',)  # Add filtering by college
    search_fields = ('name', 'college__name')  # Enable search by student name or college name
    list_per_page = 20  # Set pagination for easier navigation

