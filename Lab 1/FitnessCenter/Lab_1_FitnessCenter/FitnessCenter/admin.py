from django.contrib import admin

from FitnessCenter.models import *

class InstructorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TrainingSessionAdmin(admin.ModelAdmin):
    exclude = ['user']

    list_display = ['name', 'instructor', 'category', 'description', 'user', 'image', 'price', 'availableSpots']
    list_filter = ['category', 'instructor']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TrainingSession, TrainingSessionAdmin)