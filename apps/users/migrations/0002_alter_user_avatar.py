# Generated by Django 4.1.5 on 2023-01-31 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/default-avatar.png', null=True, upload_to='avatars', verbose_name='Avatar'),
        ),
    ]