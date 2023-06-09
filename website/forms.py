from django import forms
from .models import Posting, Reply


class PostingForm(forms.ModelForm):
    
    class Meta:
        model = Posting
        fields = ('category', 'title', 'content', )

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('content', )