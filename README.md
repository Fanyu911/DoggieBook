# DoggieBook
  steps to open DoggieBook：
  1. clone or download;
  2. install requirement.txt;
  3. makemigrations and migrate;
  4. populate by : python populate_script.py;
  5. index models by: python manage.py rebuild_index;
  6. run server.

Some Useful commands:
# python manage.py makemigrations doggie
# python manage.py migrate
# python manage.py createsuperuser
# python populate_script.py
# python manage.py runserver
# python manage.py rebuild_index
# python manage.py test doggie
# pip freeze > requirements.txt
