from django import forms
from .models import Announcement

class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = ['title','content']

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
