from django.contrib import admin
from .models import User, Barrow, Category, Books

# Register your models here.

admin.site.register(User)
admin.site.register(Barrow)
admin.site.register(Category)
admin.site.register(Books)
