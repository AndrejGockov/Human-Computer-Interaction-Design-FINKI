from django.contrib import admin

from Lab_1_BookStore.models import *

class BookAdmin(admin.ModelAdmin):
    exclude = ['userEntry']
    list_display = ['title', 'author', 'genre', 'userEntry', 'description', 'image', 'price', 'availableCopies']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.userEntry = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book, BookAdmin)