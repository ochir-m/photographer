from django import template

from photographer.models import *

register = template.Library()

@register.inclusion_tag('photographer/menu.html')
def show_menu():
    menu = [{'title': 'Портфолио', 'url_name': 'portfolio'},
            {'title': 'Контакты и цены', 'url_name': 'contacts'},
            ]
    return {'menu': menu}

@register.inclusion_tag('photographer/other_menu.html')
def other_menu():
    other_menu = [{'title': 'Акции и спецпредложения', 'url_name': 'promo'},
                  {'title': 'Подарочные сертификаты', 'url_name': 'gift'},
    ]
    return {'other_menu': other_menu}

@register.inclusion_tag('photographer/social_networks.html')
def show_social_networks():
    social_networks = [{'title': 'tg', 'url': 'https://web.telegram.org', 'class': 'bi bi-telegram'},
                       {'title': 'wa', 'url': 'https://www.whatsapp.com', 'class': 'bi bi-whatsapp'},
                       {'title': 'fb', 'url': 'https://facebook.com', 'class': 'bi bi-facebook'},
                       {'title': 'inst', 'url': 'https://www.instagram.com', 'class': 'bi bi-instagram'},
                       {'title': 'mail', 'url': 'https://mail.google.com', 'class': 'bi bi-envelope-fill'},
                       {'title': 'in', 'url': 'https://linkedin.com', 'class': 'bi bi-linkedin'},
                       {'title': 'yt', 'url': 'https://www.youtube.com', 'class': 'bi bi-youtube'},
                       {'title': 'tt', 'url': 'https://www.tiktok.com', 'class': 'bi bi-tiktok'},
                       {'title': 'pin', 'url': 'https://www.pinterest.com', 'class': 'bi bi-pinterest'},
                       {'title': 'twit', 'url': 'https://twitter.com', 'class': 'bi bi-twitter'},
    ]
    return {'social_networks': social_networks}

@register.inclusion_tag('photographer/category.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}
