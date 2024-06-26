# Generated by Django 5.0.6 on 2024-05-26 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('imageUrl', models.CharField(max_length=255)),
                ('synopsis', models.TextField()),
                ('trailerUrl', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
