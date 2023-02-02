# Generated by Django 4.1.5 on 2023-02-02 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
                'db_table': 'countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='authors', verbose_name='Foto')),
                ('birth', models.DateField(verbose_name='Fecha de nacimiento')),
                ('nacionality', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authors.countries', verbose_name='nacionalidad')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'author',
                'ordering': ['first_name'],
            },
        ),
    ]
