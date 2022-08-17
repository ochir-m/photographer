# Generated by Django 4.0.4 on 2022-07-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0005_blog_alter_subcategory_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 2'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 3'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 4'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 5'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo6',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 6'),
        ),
    ]