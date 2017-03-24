from django import forms

from blog.posts.models import Post


class PostForm(forms.Form):
    title = forms.CharField(min_length=10)
    description = forms.CharField(widget=forms.Textarea)


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
