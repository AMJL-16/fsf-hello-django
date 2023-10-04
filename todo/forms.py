from django import forms
from .models import Item


# create ItemForm class
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
