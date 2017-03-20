from django import forms

from blog.authors.models import GENDER_CHOICES, Author


class AddAuthorForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    def clean_email(self):
        email = self.cleaned_data['email']
        if Author.objects.filter(email=email).exists():
            raise forms.ValidationError('Author with email: "{}" already exists'.format(email))
        return email

    def save(self):
        cd = self.cleaned_data

        author = Author(
            first_name=cd['first_name'],last_name=cd['last_name'],
            email=cd['email'], date_of_birth=cd['date_of_birth'],
            gender=cd['gender']
        )
        author.save()

        return author


class EditAuthorEmailForm(forms.Form):
    author = forms.IntegerField(widget=forms.HiddenInput)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if Author.objects.filter(email=email).exists():
            raise forms.ValidationError('Author with email: "{}" already exists'.format(email))
        return email

    def save(self):
        cd = self.cleaned_data

        author = Author.objects.get(id=cd['author'])
        author.email = cd['email']
        author.save()

        return author
