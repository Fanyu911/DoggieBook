import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                            'doggie_project.settings')
import django
django.setup()

from doggie.models import DogCategory,Dog
def populate():
    BigDog_pages = [
        {'dog_name': 'caiquan',
         'short_description':'caiquan is here',
         'long_description':'caiquan is here',
         'body':'Big Dog',
         'price': 0
         },
         {'dog_name': 'keji',
         'short_description':'keji is here',
         'long_description':'caiquan is here',
         'body':'Big Dog',
          'price': 0
          } ]
    SmallDog_pages =[{'dog_name': 'xiaocaiquan',
         'short_description':'keji is here',
         'long_description':'caiquan is here',
         'body':'Small Dog',
          'price': 0
         },
         {'dog_name': 'xiaokeji',
          'short_description':'keji is here',
         'long_description':'caiquan is here',
         'body':'Small Dog',
         'price': 0
         } ]


    cats = {'BigDog': {'dogs': BigDog_pages,},
            'SmallDog': {'dogs': SmallDog_pages}}

    for cat ,cat_data in cats.items():
            c = add_cat(cat)
            for r in cat_data["dogs"]:
                    add_dog(c,r['dog_name'],r['short_description'],r['long_description'],r['body'],r['price'])

    # Print out the categories we have added.
    for c in DogCategory.objects.all():
            for p in Dog.objects.filter(dogcategory=c):
                print(f'- {c}: {p}')

def add_dog(cat,dog_name,short_description,long_description,body,price=0):
        r = Dog.objects.get_or_create(dogcategory=cat, dog_name=dog_name)[0]
        r.short_description = short_description
        r.long_description = long_description
        r.body = body

        r.price = price

        r.save()
        return r

def add_cat(name):
        c = DogCategory.objects.get_or_create(name=name)[0]
        c.save()
        return c



if  __name__=='__main__':
    print('Starting Doggie population script...')
    populate()

# python manage.py makemigrations doggie

# python manage.py migrate

# python manage.py createsuperuser

# python populate_doggie.py

# python manage.py runserver
