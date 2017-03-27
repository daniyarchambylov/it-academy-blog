from django import forms

from blog.authors.models import Author
from blog.posts.models import Post


class PostForm(forms.Form):
    title = forms.CharField(min_length=10)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    def save(self):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        author = self.cleaned_data['author']
        post = Post(title=title, description=description, author=author)
        post.save()
        return post


class EditPostForm(forms.Form):
    post = forms.IntegerField(widget=forms.HiddenInput)
    title = forms.CharField(min_length=10)
    description = forms.CharField(widget=forms.Textarea)
    author = forms.ModelChoiceField(queryset=Author.objects.all())

    def save(self):
        post = Post.objects.get(id=self.cleaned_data['post'])
        post.title = self.cleaned_data['title']
        post.description = self.cleaned_data['description']
        post.author = self.cleaned_data['author']
        post.save()
        return post


class PostDeleteForm(forms.Form):
    post = forms.IntegerField(widget=forms.HiddenInput)

    def clean_post(self):
        post = self.cleaned_data['post']
        if not Post.objects.filter(id=post).exists():
            raise forms.ValidationError()
        return post

    def delete(self):
        post = Post.objects.get(id=self.cleaned_data['post'])
        post.delete()
