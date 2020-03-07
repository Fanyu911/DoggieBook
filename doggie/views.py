from django.shortcuts import render
from doggie.models import DogCategory
from doggie.models import Dog
from doggie.forms import DogCategoryForm, DogForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from doggie.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from doggie.models import UserProfile
from django.views import View
from django.utils.decorators import method_decorator

def index(request):
    request.session.set_test_cookie()

    dogcategory_list = DogCategory.objects.order_by('-likes')[:5]
    dog_list = Dog.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage'] = 'Doggie！！！！!'
    context_dict['dogcategories'] = dogcategory_list
    context_dict['dogs'] = dog_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
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

@login_required
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

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'doggie/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('doggie:index'))
            else:
                return HttpResponse("Your Doggie account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'doggie/login.html')



@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('doggie:index'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()) )
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")

    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1

        request.session['last_visit'] = str(datetime.now())
    else:
        visits = 1
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect(reverse('doggie:index'))
        else:
            print(form.errors)

    context_dict = {'form': form}
    return render(request, 'doggie/profile_registration.html', context_dict)


class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({'picture': user_profile.picture})

        return (user, user_profile, form)

    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('doggie:index'))

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'doggie/profile.html', context_dict)

    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect(reverse('doggie:index'))

        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save(commit=True)
            return redirect(reverse('doggie:profile',
                                    kwargs={'username': username}))
        else:
            print(form.errors)

        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}

        return render(request, 'doggie/profile.html', context_dict)
