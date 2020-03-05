from django.urls import path
from doggie import views


app_name = 'doggie'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dogcategory/<slug:dogcategory_name_slug>/',views.show_dogcategory, name='show_dogcategory'),
    path('dogcategory/<slug:dogcategory_name_slug>/<slug:dog_name_slug>/',views.show_dog, name='show_dog'),
    path('add_dogcategory/',views.add_dogcategory,name='add_dogcategory'),
    path('add_dog/', views.add_dog, name='add_dog'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
]
