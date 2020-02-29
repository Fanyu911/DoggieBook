from django.urls import path
from doggie import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'doggie'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dogcategory/<slug:dogcategory_name_slug>/',views.show_dogcategory, name='show_dogcategory'),
    path('dogcategory/<slug:dogcategory_name_slug>/<slug:dog_name_slug>/',views.show_dog, name='show_dog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
