from django.contrib import admin
from .models import Category, Course, Contact, Branch

# Register your models here.

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Branch)
