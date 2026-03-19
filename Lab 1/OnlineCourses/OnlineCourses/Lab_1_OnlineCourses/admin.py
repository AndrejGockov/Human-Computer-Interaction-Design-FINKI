from django.contrib import admin

from Lab_1_OnlineCourses.models import *

# checks if it's a superuser before deleting
class HasDeletePermission(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

class InstructorAdmin(HasDeletePermission):
    list_display = ['firstName', 'lastName', 'biography', 'experienceLevel']

class CategoryAdmin(HasDeletePermission):
    list_display = ['name', 'description', 'isPopular']

class CourseAdmin(HasDeletePermission):
    exclude = ['courseMaker']
    list_display = ['name', 'instructor', 'courseMaker', 'category', 'description', 'image', 'price', 'availableSeats']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.courseMaker = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)