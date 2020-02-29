from django.contrib import admin

# Register your models here.
from django.contrib import admin
from doggie.models import DogCategory, Dog

class DogAdmin(admin.ModelAdmin):
    list_display = ('dog_name', 'dogcategory', 'short_description', 'views', 'likes')

admin.site.register(DogCategory)
admin.site.register(Dog,DogAdmin)
