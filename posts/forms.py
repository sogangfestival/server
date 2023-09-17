from django import forms
from .models import *

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['place'].required = False
        self.fields['type'].required = False
        self.fields['color'].required = False