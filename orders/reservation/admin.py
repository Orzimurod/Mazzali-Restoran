from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date', 'time', 'people', 'message')  
    search_fields = ('name', 'email')
    list_filter = ('date', 'time')
    ordering = ('-date',)
    

