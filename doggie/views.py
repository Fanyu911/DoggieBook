from django.shortcuts import render
from doggie.models import DogCategory
from doggie.models import Dog
from doggie.forms import DogCategoryForm, DogForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):

    dogcategory_list = DogCategory.objects.order_by('-likes')[:5]
    dog_list = Dog.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Doggie！！！！!'
    context_dict['dogcategories'] = dogcategory_list
    context_dict['dogs'] = dog_list
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
        context_dict['dog'] = dog

    except Dog.DoesNotExist:

        context_dict['dog'] = None

    return render(request, 'doggie/dog.html', context=context_dict)

def add_dogcategory(request):
    form = DogCategoryForm()

    if request.method == 'POST':
        form = DogCategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('doggie:index'))
        else:
            print(form.errors)
    return render(request, 'doggie/add_dogcategory.html', {'form': form})

def add_dog(request):
    form = DogForm()
    if request.method == 'POST':
        form = DogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('doggie:index'))
        else:
            print(form.errors)
    return render(request, 'doggie/add_dog.html', {'form': form})
