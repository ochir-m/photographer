from django import forms
from .models import *
from captcha.fields import CaptchaField

class MakeRequestForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = MakeRequest
        fields = ['name', 'e_mail', 'phone_number', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ВАШЕ ИМЯ', 'class': 'contacts'}),
            'e_mail': forms.EmailInput(attrs={'placeholder': 'E-MAIL', 'class': 'contacts'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'НОМЕР ТЕЛЕФОНА *', 'class': 'contacts'}),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'placeholder': 'КОММЕНТАРИЙ *: УКАЖИТЕ ЖЕЛАЕМУЮ ДАТУ, ТЕМАТИКУ СЪЕМКИ И ДРУГУЮ ВАЖНУЮ ИНФОРМАЦИЮ'}),
        }


