from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class DogCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'DogCategories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(DogCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dog(models.Model):
    dogcategory = models.ForeignKey(DogCategory, on_delete=models.CASCADE)
    dog_name = models.CharField(max_length=128, unique=True)
    short_description = models.CharField(max_length=1280)
    long_description = models.CharField(max_length=1280)
    life_span = models.CharField(max_length=128)
    price = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    images = models.ImageField(upload_to='dogs_images', null=True, blank=True)
    slug = models.SlugField(unique=True)
    dogcategory_slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dog_name)
        self.dogcategory_slug = slugify(self.dogcategory)
        super(Dog, self).save(*args, **kwargs)

    def __str__(self):
        return self.dog_name

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论人')
    body = models.TextField('评论内容')
    create_date = models.DateTimeField('评论时间', auto_now_add=True)
    belong = models.ForeignKey(settings.DOG_MODEL, on_delete=models.CASCADE, related_name='dogs_comments', verbose_name='所属文章')

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name
        ordering = ['create_date']
