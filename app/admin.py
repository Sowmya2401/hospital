from django.contrib import admin
from . models import Department, Doctor,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('p_name','p_phone','p_doctor','p_date','p_email')
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Booking, BookingAdmin)
