# Generated by Django 3.1.3 on 2021-03-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210318_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetail',
            name='image',
            field=models.ImageField(default='images/book-open.png', upload_to='books_img'),
        ),
    ]