from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("image1","image2","image3","image4","image5")