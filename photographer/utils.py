from .models import *


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        subcats = Subcategory.objects.all()
        context['cats'] = cats
        context['subcats'] = subcats
        if 'cat_selected' not in context:
            context['cat_selected'] = -1
        return context

class SliderMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        slider_photos = MainSlider.objects.filter(is_published=True)
        context['slider_photos'] = slider_photos
        return context

class ContactsMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        inst_slider_photos = InstSlider.objects.all()
        price_categories = PriceCategory.objects.all()
        price_info = Price.objects.all()
        context['inst_slider_photos'] = inst_slider_photos
        context['price_categories'] = price_categories
        context['price_info'] = price_info
        return context


class CategoryDataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        subcats = Subcategory.objects.filter(cat__slug=self.kwargs['cat_slug'])
        context['cats'] = cats
        c_name = Category.objects.filter(slug=self.kwargs['cat_slug'])
        context['title'] = str(c_name[0])
        context['subcats'] = subcats
        if 'cat_selected' not in context:
            context['cat_selected'] = -1
        return context

class SubcategoryDataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        subcats = Subcategory.objects.filter(cat__slug=self.kwargs['cat_slug'])
        context['cats'] = cats
        context['subcats'] = subcats
        if 'subcat_selected' not in context:
            context['subcat_selected'] = -1
        return context

