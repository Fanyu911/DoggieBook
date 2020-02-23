# Generated by Django 2.1.5 on 2020-02-23 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dog_name', models.CharField(max_length=128, unique=True)),
                ('description', models.CharField(max_length=1280)),
                ('body', models.CharField(max_length=128)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name_plural': 'DogCategories',
            },
        ),
        migrations.AddField(
            model_name='dog',
            name='dogcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doggie.DogCategory'),
        ),
    ]
