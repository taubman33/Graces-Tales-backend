# Generated by Django 4.0.4 on 2022-05-06 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tales', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='no genre', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.CharField(default='no price', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.CharField(default='no summary', max_length=250),
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='no title', max_length=50),
        ),
    ]
