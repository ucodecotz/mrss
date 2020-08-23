from django import forms
from .models import *

DEVICE_TYPE_CHOICE = (
    ('A', 'Android'),
    ('I', 'Ios')
)

DEVICE_BRAND_CHOICE = (
    ('T', 'Teckno'),
    ('S', 'Samsung'),
    ('U', 'Huawei'),
    ('O', 'Oppo'),

)


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())


class ProblemForm(forms.Form):
    title = forms.CharField( label='Problem title',widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    image = forms.FileField(label='Problem image',widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    problem_desc = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'cols': 25,
        'rows': 4
    }))
    device_type = forms.ChoiceField(choices=DEVICE_TYPE_CHOICE, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    device_brand = forms.ChoiceField(choices=DEVICE_BRAND_CHOICE, widget=forms.Select(attrs={
        'class': 'form-control'
    }))


class AddSolutionForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Add your Solution to this problem',
        'cols': 100
    }))
