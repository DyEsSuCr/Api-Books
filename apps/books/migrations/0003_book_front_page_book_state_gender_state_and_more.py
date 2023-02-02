# Generated by Django 4.1.5 on 2023-02-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_lenguaje_remove_book_lenguaje_book_lenguaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='front_page',
            field=models.ImageField(blank=True, null=True, upload_to='frontpage', verbose_name='Portada'),
        ),
        migrations.AddField(
            model_name='book',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gender',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='lenguaje',
            name='state',
            field=models.BooleanField(default=False),
        ),
    ]
