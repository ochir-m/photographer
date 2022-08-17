from django.db import models
from django.urls import reverse

class Photos(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название фото')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время загрузки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    subcat = models.ForeignKey('Subcategory', on_delete=models.PROTECT, null=True, verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Subcategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Подкатегория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория', related_name='sub')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'cat_slug': self.cat.slug,
                                              'subcat_slug': self.slug})

    class Meta:
        verbose_name = 'Подкатегории'
        verbose_name_plural = 'Подкатегории'
        ordering = ['id']


class Blog(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Заголовок')
    describe = models.CharField(max_length=255, db_index=True, null=True, verbose_name='Описание статьи')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content1 = models.TextField(verbose_name='Инфа1', null=True)
    content2 = models.TextField(verbose_name='Инфа2', blank=True)
    content3 = models.TextField(verbose_name='Инфа3', blank=True)
    content4 = models.TextField(verbose_name='Инфа4', blank=True)
    content5 = models.TextField(verbose_name='Инфа5', blank=True)
    content6 = models.TextField(verbose_name='Инфа6', blank=True)
    photo1 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 1 (обложка)', null=True)
    photo2 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 2', null=True, blank=True)
    photo3 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 3', null=True, blank=True)
    photo4 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 4', null=True, blank=True)
    photo5 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 5', null=True, blank=True)
    photo6 = models.ImageField(upload_to='blog_photos/%Y/%m/%d/', verbose_name='Фото 6', null=True, blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время загрузки')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    url = models.URLField(max_length=100, blank=True, verbose_name='Сайт для статьи')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
        ordering = ['time_create', 'title']


class Promo(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='promo_photos/%Y/%m/%d/', verbose_name='Фото (обложка)', null=True)
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акции'
        verbose_name_plural = 'Акции'
        ordering = ['-date_start', 'title']


class Gift(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(null=True)
    content = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='gift_photos/%Y/%m/%d/', verbose_name='Фото (обложка)', null=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Подарочные сертификаты'
        verbose_name_plural = 'Подарочные сертификаты'
        ordering = ['title', 'price']


class MainSlider(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    photo = models.ImageField(upload_to='main_slider/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото для главного слайдера'
        verbose_name_plural = 'Фото для главного слайдера'
        ordering = ['name']

class InstSlider(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    photo = models.ImageField(upload_to='inst_slider/%Y/%m/%d/', verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото для инста-слайдера'
        verbose_name_plural = 'Фото для инста-слайдера'
        ordering = ['id']

class Price(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(null=True, verbose_name='Цена')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    price_cats = models.ForeignKey('PriceCategory', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прайс-лист'
        verbose_name_plural = 'Прайс-лист'
        ordering = ['id']

class PriceCategory(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    photo = models.ImageField(upload_to='price_list/%Y/%m/%d/', verbose_name='Обложка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Прайс категории'
        verbose_name_plural = 'Прайс категории'
        ordering = ['id']


class MakeRequest(models.Model):
    name = models.CharField(max_length=100, db_index=True, blank=True, verbose_name='Имя')
    e_mail = models.EmailField(max_length=100, db_index=True, blank=True, verbose_name='E-mail')
    phone_number = models.CharField(max_length=40, db_index=True, verbose_name='Номер телефона')
    comment = models.TextField(verbose_name='Комментарий')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время оформления')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    done = models.BooleanField(default=False, verbose_name='Заявка обработана')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts')

    class Meta:
        verbose_name = 'Заявки на съемку'
        verbose_name_plural = 'Заявки на съемку'
        ordering = ['-time_create']


