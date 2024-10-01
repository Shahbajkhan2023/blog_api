from django import forms
from .models import Profile, Post
from django.core.exceptions import ValidationError


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_image', 'social_link']

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        
        # Minimum length validation
        if bio and len(bio) < 400:
            raise ValidationError('Bio must be at least 400 characters long.')
        
        return bio
    

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'image', 'category', 'tags', 'is_published']
    
