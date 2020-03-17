
from django.test import TestCase
from doggie.models import Dog,DogCategory


def add_dogcategory(name, views=0):
    dogcategory = DogCategory.objects.get_or_create(name=name)[0]
    dogcategory.views = views
    dogcategory.save()
    return dogcategory

def add_dog(dogcategory, dog_name,likes =0):
    return Dog.objects.get_or_create(dogcategory = dogcategory, dog_name=dog_name ,likes =likes)[0]


class DogMethodTests(TestCase):

    def test_ensure_likes_are_positive(self):
        """Ensures the number of likes are postive or zero"""
        dogcat = add_dogcategory(name ='test')
        dog = add_dog(dog_name='test',likes = -1,dogcategory= dogcat)
        self.assertEqual((dog.likes >= 0), True)

    def test_slug_line_creation(self):
        """Check slug"""
        dog = add_dogcategory(name='Random Dog String')
        self.assertEqual(dog.slug, 'random-dog-string')

class DogCategoryMethodTests(TestCase):

     def test_slug_line_creation(self):
        """Check slug"""
        category = add_dogcategory(name='Random Category String')
        self.assertEqual(category.slug, 'random-category-string')
