# Generated by Django 4.2.3 on 2023-08-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0003_book_description_book_imgae_book_number_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type',
            field=models.TextField(default='Dev'),
        ),
    ]