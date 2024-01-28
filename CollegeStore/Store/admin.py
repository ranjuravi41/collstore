from django.contrib import admin
from .models import Department, Course, Order

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Order)