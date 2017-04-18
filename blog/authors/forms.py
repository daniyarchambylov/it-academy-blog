import datetime

import re
from django import forms
from django.contrib.auth import get_user_model

from blog.authors.models import GENDER_CHOICES, Author


User = get_user_model()


class AddAuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author

        fields = [
            'date_of_birth',
            'gender',
            'image',
        ]
        error_messages = {
            'unique': 'Email bla bla bla'
        }

    def __init__(self, *args, **kwargs):
        super(AddAuthorModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
        ]



class AddAuthorForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    def clean_date_of_birth(self):
        db = self.cleaned_data['date_of_birth']
        date = datetime.date(1960, 01, 01)
        if db < date:
            raise forms.ValidationError('Date of birth can not be less than 1960-01-01.')
        return db

    def clean(self):
        cd = super(AddAuthorForm, self).clean()
        errors = []

        test = re.match(r'^[A-Z][a-z]+$', cd['first_name'].strip()) and \
               re.match(r'^[A-Z][a-z]+$', cd['last_name'].strip())

        if not test:
            errors.append('First name or last name are incorrect.')

        if cd['gender'] == 'm':
            errors.append('Gender can not be equal to "m"')

        if len(errors) > 0:
            raise forms.ValidationError(errors)

        return cd

    def save(self):
        cd = self.cleaned_data

        author = Author(
            first_name=cd['first_name'],last_name=cd['last_name'],
            email=cd['email'], date_of_birth=cd['date_of_birth'],
            gender=cd['gender']
        )
        author.save()

        return author


class EditAuthorEmailModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
