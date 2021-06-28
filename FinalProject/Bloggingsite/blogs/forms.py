from django import forms
from django.forms import fields, widgets
from .models import BlogPost
class new_post_form(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','text']
        widgets = {'text':forms.Textarea(attrs={'cols':100})}
class edit_post_form(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['text']
        widgets = {'text':forms.Textarea(attrs={'cols':100})}