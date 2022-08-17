# Generated by Django 4.0.4 on 2022-07-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0008_gift'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gift',
            options={'ordering': ['title', 'price'], 'verbose_name': 'Подарочные сертификаты', 'verbose_name_plural': 'Подарочные сертификаты'},
        ),
        migrations.AddField(
            model_name='gift',
            name='price',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
