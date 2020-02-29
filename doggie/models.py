from django.db import models

# Create your models here.
class DogCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'DogCategories'
        
    def __str__(self):
        return self.name

class Dog(models.Model):
    dogcategory = models.ForeignKey(DogCategory, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=128, unique=True)
    short_description = models.CharField(max_length=1280)
    long_description = models.CharField(max_length=1280)
    body = models.CharField(max_length=128)
    price = models.IntegerField(default=0)


    def __str__(self):
        return self.dog_name
