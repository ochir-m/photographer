from django.http import HttpResponseNotFound
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from .forms import *
from .models import *
from .utils import DataMixin, CategoryDataMixin, SubcategoryDataMixin, SliderMixin, ContactsMixin


class PhotographerHome(SliderMixin, ListView):
    paginate_by = 3
    model = Blog
    template_name = 'photographer/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Фотограф Очир Манджиев')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)


class ShowPost(DetailView):
    model = Blog
    template_name = 'photographer/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        return context


class Contacts(ContactsMixin, SuccessMessageMixin, CreateView):
    form_class = MakeRequestForm
    template_name = 'photographer/contacts.html'
    success_message = "Заявка успешно отправлена. Свяжусь с вами в течение 24 часов."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты и цены')
        return dict(list(context.items()) + list(c_def.items()))


def show_pd(request):
    title = 'Согласие на обработку персональных данных'
    return render(request, 'photographer/pd.html', {'title': title})


class Portfolio(DataMixin, ListView):
    model = Photos
    template_name = 'photographer/portfolio.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Портфолио')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Photos.objects.filter(is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")


class Category(CategoryDataMixin, ListView):
    model = Photos
    template_name = 'photographer/portfolio.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Photos.objects.filter(subcat__cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(cat_selected=context['posts'][0].subcat_id)
        return dict(list(context.items()) + list(c_def.items()))


class Subcategory(SubcategoryDataMixin, ListView):
    model = Photos
    template_name = 'photographer/portfolio.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Photos.objects.filter(subcat__slug=self.kwargs['subcat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=str(context['posts'][0].subcat),
                                      subcat_selected=context['posts'][0].subcat_id)
        return dict(list(context.items()) + list(c_def.items()))


class MyPromo(ListView):
    model = Promo
    template_name = 'photographer/promo.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Акции и спецпредложения'
        return context

    def get_queryset(self):
        return Promo.objects.filter(is_published=True)


class GiftCertificate(ListView):
    model = Gift
    template_name = 'photographer/gift.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Gift.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Подарочные сертификаты'
        return context
