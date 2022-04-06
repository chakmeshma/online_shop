from django import forms
from .models import *


class ItemRequestForm(forms.ModelForm):
    class Meta:
        model = ItemRequest
        fields = '__all__'
        labels = {'link': 'لینک',
                  'price': 'قیمت',
                  'weight': 'وزن',
                  'count': 'تعداد',
                  'description': 'توضیحات'}
