# Generated by Django 4.0.4 on 2022-06-01 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MakeRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Имя')),
                ('e_mail', models.EmailField(db_index=True, max_length=100, verbose_name='E-mail')),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=40, verbose_name='Номер телефона')),
                ('comment', models.TextField(blank=True, verbose_name='Комментарий')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время обновления')),
                ('done', models.BooleanField(default=False, verbose_name='Заявка обработана')),
            ],
            options={
                'verbose_name': 'Заявки на съемку',
                'verbose_name_plural': 'Заявки на съемку',
                'ordering': ['-time_create'],
            },
        ),
    ]
