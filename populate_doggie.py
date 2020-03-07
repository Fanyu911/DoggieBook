import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'doggie_project.settings')
import django

django.setup()

from doggie.models import DogCategory, Dog


def populate():
    BigDog_pages = [
        {'dog_name': 'Alaskan Malamute',
         'short_description': 'The Alaskan Malamute is powerful, independent, strong willed, and fun loving.',
         'long_description': 'The breed’s origin is unknown, but was first described living among the native Inuit '
                             'people known as the Mahlemuts, who lived along Norton Sound on Alaska’s northwest '
                             'coast. Given the dog’s history as a sled dog, the malamute loves activity and '
                             'interaction with the family. Malamutes are family oriented, and as long as they are '
                             'given daily exercise, they are well-mannered in the home. Without proper exercise, '
                             'they can become frustrated and destructive. This dog is friendly and sociable toward '
                             'people, but may be assertive and should be introduced carefully to new dogs, pets, '
                             'or livestock. Some can be domineering, and tend to dig and howl.',
         'life_span': '10 to 12 years',
         'price': 400, 'views': 2, 'images': 'Alaskan Malamute.jpg'
         },
        {'dog_name': 'Golden Retriever',
         'short_description': 'Everybody’s friend, the Golden Retrievers are known for their devoted and obedient '
                              'nature as a family companion. ',
         'long_description': 'With an increasing interest in retrieving dogs in the mid-1800s, Lord Tweedmouth bred '
                             'Nous, a yellow Wavy-Coated Retriever (a descendant of the small Newfoundland and the '
                             'earlier Labrador breeds used by fisherman) to Belle, a Tweed Water Spaniel (a popular '
                             'liver-colored retriever with tightly curled coat). This dog is an apt sporting '
                             'retriever as well and yearns for a day in the field. Ignoring the Golden’s active '
                             'nature and powerful physique can lead to behavior problems, and therefore they need '
                             'daily physical and mental exercise. Some Goldens may be overly exuberant and '
                             'boisterous, but most are eager to please and enjoy learning.',
         'life_span': '10 to 13 years',
         'price': 800, 'views': 2, 'images': 'Golden Retriever.jpg'

         },
        {'dog_name': 'Samoyed',
         'short_description': 'Gentle and playful, the Samoyed often makes a good companion for a child or person of '
                              'any age.',
         'long_description': 'The nomadic Samoyed people, for whom the Samoyed dog is named, came to northwestern '
                             'Siberia from central Asia. They are a closely bonded family dog. They are generally '
                             'amiable with strangers, other pets, and usually, other dogs. They can be calm indoors, '
                             'but this clever, sometimes mischievous breed needs daily physical and mental exercise. '
                             'If allowed to become bored, they will dig and bark. They are independent and often '
                             'stubborn, but they are willing to please and responsive to their family.  They may tend '
                             'to herd children.',
         'life_span': '10 to 12 years',
         'price': 2000, 'views': 2, 'images': 'Samoyed.jpg'
         },
        {'dog_name': 'Belgian Shepherd / Malinois',
         'short_description': 'Intense best describes the Belgian Malinois.',
         'long_description': 'The Belgian sheepherding breeds, collectively known as Chiens de Berger Belge, '
                             'shared their early history as general-purpose shepherds and guard dogs of Belgium. This '
                             'is a high-energy breed with a need for regular mental and physical stimulation. These '
                             'dogs are alert, smart, and serious. They can be aloof with strangers and should be '
                             'introduced to other dogs and animals carefully. Some can be domineering. When confined, '
                             'they often run in sweeping circles in an effort to stay on the move. They are '
                             'protective of their home and family.',
         'life_span': '10 to 12 years',
         'price': 1000, 'views': 2, 'images': 'Belgian Shepherd : Malinois.jpg'
         }]
    SmallDog_pages = [{'dog_name': 'French Bulldog',
                       'short_description': 'He is a fabulous family friend and show dog.',
                       'long_description': 'The French Bulldog has enjoyed a long history as a companion dog. Created '
                                           'in England to be a miniature Bulldog, he accompanied English lacemakers '
                                           'to France, where he acquired his Frenchie moniker. Besides being a '
                                           'companion, he once served as an excellent ratter, but today his job '
                                           'focuses on being a fabulous family friend and show dog. He’s a rare dog '
                                           'breed, so expect to put in some time on a waiting list before you’re able '
                                           'to bring one home.',
                       'life_span': '11 to 14 years',
                       'price': 200, 'views': 2, 'images': 'French Bulldog.jpg'
                       },
                      {'dog_name': 'Border Terrier',
                       'short_description': 'The Border is one of the most amiable and tractable of the Terrier group.',
                       'long_description': 'Perhaps the oldest of Britain’s terriers, the Border Terrier originated '
                                           'around the Cheviot Hills forming the border country between Scotland and '
                                           'England. This breed is inquisitive, busy, friendly, and biddable. They do '
                                           'like to track and can be independent, ingredients that make for a dog '
                                           'that may tend to roam if given the chance. Borders are generally good '
                                           'with other dogs and cats, but not with small animals. They are very good '
                                           'with children and make a good companion for people of all ages. They dig, '
                                           'and some bark. Some are talented escape artists.',
                       'life_span': '12 to 15 years',
                       'price': 500, 'views': 2, 'images': 'Border Terrier.jpg'
                       },
                      {'dog_name': 'Bichon Frise',
                       'short_description': 'kPerky, bouncy, and playful, the Bichon Frise’s happy-go-lucky outlook '
                                            'is endearing to all.',
                       'long_description': 'The Bichon Frise has roots in the Mediterranean, originally produced by '
                                           'crossing the Barbet (a large water dog) with small coated, often white '
                                           'dogs.The striking powder-puff appearance of the Bichon derives from a '
                                           'double coat, with a soft dense undercoat and coarser, curly outercoat, '
                                           'causing the coat to stand off the body and even spring back when patted. '
                                           'This is a merry, agile breed with an effortless and efficient gait. The '
                                           'Bichon’s looks and fitness make this sturdy little dog a popular family '
                                           'addition. The soft, inquisitive expression enables this breed to worm its '
                                           'way into many hearts and laps.',
                       'life_span': '12 to 15 years',
                       'price': 500, 'views': 2, 'images': 'Bichon Frise.jpg'
                       },
                      {'dog_name': 'Maltese',
                       'short_description': 'Long a favorite lapdog, the gentle Maltese fills this role admirably.',
                       'long_description': 'The Maltese is the most ancient of the European toy breeds, and among the '
                                           'oldest of all breeds. The Maltese also has a wild side, and loves to run '
                                           'and play. Despite the innocent look, this is bold and feisty pup who may '
                                           'challenge larger dogs, and some enjoy barking. The Maltese is reserved '
                                           'with strangers. The exercise requirements of the Maltese are easily met '
                                           'with indoor games, a romp in the yard, or a short walk on leash.',
                       'life_span': '12 to 14 years',
                       'price': 1000, 'views': 2, 'images': 'Maltese.jpg'
                       }]

    MidDog_pages = [{'dog_name': 'American Eskimo Dog',
                     'short_description': 'The American Eskimo is bright, eager to please, lively, and fun loving—in '
                                          'short, an enjoyable and generally obedient companion. ',
                     'long_description': 'As the prototypical spitz, the Eskie (as this breed is often called) is '
                                         'just as often simply called spitz by pet households. True to this dog’s '
                                         'spitz heritage, The Eskie is independent and tenacious and loves to run, '
                                         'especially in cold weather. They are among the most biddable of spitz '
                                         'breeds, and are calm and well-mannered inside. Because of their watchdog '
                                         'origins, Eskies can be wary of strangers, and may not be the best choice '
                                         'for homes with small children, other dogs, or pets unless well supervised.',
                     'life_span': '12 to 14 years',
                     'price': 600, 'views': 2, 'images': 'American Eskimo.jpg'
                     },
                    {'dog_name': 'Australian Cattle Dog',
                     'short_description': 'Smart, hardy, independent, stubborn, tenacious, energetic, and untiring— '
                                          'these are all traits essential to a driver of headstrong cattle, '
                                          'and all traits of the Australian Cattle Dog.',
                     'long_description': 'In 1840, a dog was needed that could withstand traveling long distances '
                                         'over rough terrain in hot weather and that could control cattle without '
                                         'barking (which only served to make wild cattle wilder) in Australia. Given '
                                         'challenging mental and hard physical exercise daily, this breed is among '
                                         'the most responsive and obedient of dogs. The Cattle Dog tends to nip at '
                                         'heels of running children, but is good with older children.',
                     'life_span': '10 to 13 years',
                     'price': 300, 'views': 2, 'images': 'Australian Cattle Dog.jpg'
                     },
                    {'dog_name': 'Border Collie',
                     'short_description': 'The Border Collie is a bundle of mental and physical energy awaiting a '
                                          'chance to be unleashed on the world. ',
                     'long_description': 'The consummate sheepdog, the Border Collie is the result of over a century '
                                         'of breeding for function above all other criteria in the 1800s. Among the '
                                         'most intelligent and obedient of breeds, the BC is nonetheless a disastrous '
                                         'family member if not given a challenging job every day. Given sufficient '
                                         'exercise, they are dependable and loyal companions. They are intent on '
                                         'whatever they do and tend to stare, which can be unnerving to other '
                                         'animals. They also like to chase other animals. They are reserved, '
                                         'even protective, toward strangers. Without a job, BCs can be destructive '
                                         'and can develop harmful, compulsive habits.',
                     'life_span': '10 to 14 years',
                     'price': 450, 'views': 2, 'images': 'Border Collie.jpg'
                     },
                    {'dog_name': 'Siberian Husky',
                     'short_description': 'Fun-loving, adventurous, alert, independent, clever, stubborn, '
                                          'mischievous, and obstinate all describe the Siberian Husky.',
                     'long_description': 'The Chukchi people of northeast Asia developed the breed now known as the '
                                         'Siberian Husky. This breed loves to run and will roam if given the chance. '
                                         'They may be very assertive toward strange dogs, but they are generally good '
                                         'with other dogs in the home. In fact, they are very social and must have '
                                         'lots of human or canine companionship. They may chase strange cats or small '
                                         'pets. Some are likely to howl, dig, and chew.',
                     'life_span': '11 to 13 years',
                     'price': 500, 'views': 2, 'images': 'Siberian Husky.jpg'
                     }]

    cats = {'BigDog': {'dogs': BigDog_pages },
            'SmallDog': {'dogs': SmallDog_pages },
            'MidDog': {'dogs': MidDog_pages }}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for r in cat_data["dogs"]:
            add_dog(c, r['dog_name'], r['short_description'], r['long_description'], r['life_span'], r['price'], r['views'], r['images'])

    # Print out the categories we have added.
    for c in DogCategory.objects.all():
        for p in Dog.objects.filter(dogcategory=c):
            print(f'- {c}: {p}')


def add_dog(cat, dog_name, short_description, long_description, life_span, price=0, views=0, images =''):
    r = Dog.objects.get_or_create(dogcategory=cat, dog_name=dog_name)[0]
    r.short_description = short_description
    r.long_description = long_description
    r.life_span = life_span
    r.price = price
    r.views = views
    r.images = images
    r.save()
    return r


def add_cat(name,views=0):
    c = DogCategory.objects.get_or_create(name=name)[0]
    c.views = views
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Doggie population script...')
    populate()

# python manage.py makemigrations doggie

# python manage.py migrate

# python manage.py createsuperuser

# python populate_doggie.py

# python manage.py runserver
