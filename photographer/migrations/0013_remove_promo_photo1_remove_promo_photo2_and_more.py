# Generated by Django 4.0.4 on 2022-07-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0012_pricecategory_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promo',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='photo4',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='photo5',
        ),
        migrations.RemoveField(
            model_name='promo',
            name='photo6',
        ),
        migrations.AddField(
            model_name='promo',
            name='photo',
            field=models.ImageField(null=True, upload_to='promo_photos/%Y/%m/%d/', verbose_name='Фото (обложка)'),
        ),
    ]
