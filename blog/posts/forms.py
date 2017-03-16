from django import forms


class PostForm(forms.Form):
    title = forms.CharField(min_length=10)
    description = forms.CharField(widget=forms.Textarea)
