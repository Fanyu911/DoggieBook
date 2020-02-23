import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                            'doggie_project.settings')
import django
django.setup()

from doggie.models import DogCategory,Dog
def populate():
    BigDog_pages = [
        {'dog_name': 'caiquan',
         'description':'caiquan is here',
         'body':'Big Dog',
         'price': 0
         },
         {'dog_name': 'keji',
         'description':'keji is here',
         'body':'Big Dog',
          'price': 0
          } ]
    SmallDog_pages =[{'dog_name': 'xiaocaiquan',
         'description':'xiaocaiquan is here',
         'body':'Small Dog',
          'price': 0
         },
         {'dog_name': 'xiaokeji',
         'description':'xiaokeji is here',
         'body':'Small Dog',
         'price': 0
         } ]


    cats = {'BigDog': {'dogs': BigDog_pages,},
            'SmallDog': {'dogs': SmallDog_pages}}

    for cat ,cat_data in cats.items():
            c = add_cat(cat)
            for r in cat_data["dogs"]:
                    add_dog(c,r['dog_name'],r['description'],r['body'],r['price'])

    # Print out the categories we have added.
    for c in DogCategory.objects.all():
            for p in Dog.objects.filter(dogcategory=c):
                print(f'- {c}: {p}')

def add_dog(cat,dog_name,description,body,price=0):
        r = Dog.objects.get_or_create(dogcategory=cat, dog_name=dog_name)[0]
        r.description = description
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
