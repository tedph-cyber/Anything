from django import forms
from .models import Section, Post

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'slug']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'section']   