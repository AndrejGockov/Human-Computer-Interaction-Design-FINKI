from django.contrib import admin

from Lab_1_RestarauntApp.models import *

class CuisineAdmin(admin.ModelAdmin):
    list_display = ['name']

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name']

class ReservationAdmin(admin.ModelAdmin):
    exclude = ['reservationHolder']
    list_display = ['reservationHolder', 'restaurant', 'date', 'numGuests', 'specialRequests', 'status', 'price']
    list_filter = ['status']

    def save_model(self, request, obj, form, change):
        if(not obj.pk):
            obj.reservationHolder = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Reservation, ReservationAdmin)
