from django import forms
from django import forms

class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Description")