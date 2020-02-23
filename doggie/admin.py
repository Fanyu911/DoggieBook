from django.contrib import admin

# Register your models here.
from django.contrib import admin
from doggie.models import DogCategory, Dog

admin.site.register(DogCategory)
admin.site.register(Dog)
