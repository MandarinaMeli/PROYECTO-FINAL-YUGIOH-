# Generated by Django 5.0 on 2024-01-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('invocacion', models.CharField(max_length=40)),
                ('personajes', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('invocacion', models.CharField(max_length=40)),
                ('personajes', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('año', models.IntegerField()),
                ('invocacion', models.CharField(max_length=40)),
                ('personajes', models.CharField(max_length=40)),
            ],
        ),
    ]
