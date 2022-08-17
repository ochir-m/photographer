from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    fields = ('title', 'subcat', 'content', 'photo', 'get_mini_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_mini_photo')

    def get_mini_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'time_create', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

    def get_mini_photo(self, object):
        if object.photo1:
            return mark_safe(f"<img src='{object.photo1.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)

    def get_mini_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'

class PriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'is_published', 'price_cats')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'price')

class PriceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_mini_photo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('name',)
    fields = ('name', 'photo', 'get_mini_photo')
    readonly_fields = ('get_mini_photo',)

    def get_mini_photo(self, object):
        return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'


class InstSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_editable = ('is_published',)
    list_filter = ('is_published',)

    def get_mini_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'


class PromoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_start', 'date_end', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'date_start', 'date_end', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'date_start', 'date_end')
    prepopulated_fields = {"slug": ("title",)}

    def get_mini_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'

class GiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_mini_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', )
    prepopulated_fields = {"slug": ("title",)}

    def get_mini_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
    get_mini_photo.short_description = 'Миниатюра'

class MakeRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'e_mail', 'phone_number', 'comment', 'time_create', 'time_update', 'done')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'e_mail', 'phone_number', 'comment')
    list_editable = ('done', )
    list_filter = ('done', 'time_create')

admin.site.register(Photos, PhotosAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(MainSlider, MainSliderAdmin)
admin.site.register(InstSlider, InstSliderAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(Gift, GiftAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(PriceCategory, PriceCategoryAdmin)
admin.site.register(MakeRequest, MakeRequestAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Админ-панель сайта'
admin.site.site_header = 'Админ-панель сайта'