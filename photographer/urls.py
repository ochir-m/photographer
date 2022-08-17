from django.urls import path
from django.views.decorators.cache import cache_page
from .views import *

urlpatterns = [
    path('', cache_page(60*10)(PhotographerHome.as_view()), name='home'),
    path('portfolio/', cache_page(60*10)(Portfolio.as_view()), name='portfolio'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('post/<slug:post_slug>/', cache_page(60*10)(ShowPost.as_view()), name='post'),
    path('portfolio/<slug:cat_slug>/', cache_page(60*10)(Category.as_view()), name='category'),
    path('portfolio/<slug:cat_slug>/<slug:subcat_slug>/', cache_page(60*10)(Subcategory.as_view()), name='subcategory'),
    path('promo/', cache_page(60*10)(MyPromo.as_view()), name='promo'),
    path('gift/', cache_page(60*10)(GiftCertificate.as_view()), name='gift'),
    path('pd/', cache_page(60*10)(show_pd), name='pd'),
]

