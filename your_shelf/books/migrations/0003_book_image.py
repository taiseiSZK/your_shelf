# Generated by Django 2.1.7 on 2019-07-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_user_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='画像'),
        ),
    ]
