from django.shortcuts import render
from doggie.models import DogCategory
from doggie.models import Dog

from django.http import HttpResponse

def index(request):
    dogcategory_list = DogCategory.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['dogcategories'] = dogcategory_list
    return render(request, 'doggie/index.html', context=context_dict)

def about(request):
    return render(request, 'doggie/about.html')


def show_dogcategory(request, dogcategory_name_slug):
    context_dict = {}
    try:
        dogcategory = DogCategory.objects.get(slug=dogcategory_name_slug)
        dog = Dog.objects.filter(dogcategory=dogcategory)
        context_dict['dogs'] = dog
        context_dict['dogcategory'] = dogcategory
    except DogCategory.DoesNotExist:
        context_dict['dogcategory'] = None
        context_dict['dogs'] = None

    return render(request, 'doggie/dogcategory.html', context=context_dict)

def show_dog(request,dogcategory_name_slug, dog_name_slug):

    context_dict = {}

    try:

        dog = Dog.objects.filter(slug=dog_name_slug)
        context_dict['dogs'] = dog

    except DogCategory.DoesNotExist:

        context_dict['dogs'] = None

    return render(request, 'doggie/dog.html', context=context_dict)
