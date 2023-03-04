# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 11:48:37 2023

@author: haruna
"""

from django import forms
from .models import Flashcard
from django.contrib.auth.forms import AuthenticationForm

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields=('word','description',)
        
        widgets = {
            'word': forms.Textarea(attrs={'rows':1, 'cols':100}),
            'description': forms.Textarea(attrs={'rows':30, 'cols':100}),
        }
        
class FindForm(forms.Form):
    find=forms.CharField(label='Find',required=False)
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"]="form-control"