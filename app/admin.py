from django.contrib import admin
from .models import Rate, Shelter, Category, Animal
# Register your models here.

admin.site.register(Rate)
admin.site.register(Shelter)
admin.site.register(Category)
admin.site.register(Animal)

