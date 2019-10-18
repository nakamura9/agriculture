from django import forms
from common.models import Profile
from crispy_forms.layout import Layout, Row, Column, HTML, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    
    class Meta:
        model = Profile
        exclude = "user",

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'date_of_birth',
            Row(
                Column('photo', css_class='col-6'),
                Column('bio', css_class='col-6'),
            ),
            Row(
                Column('password', css_class='col-6'),
                Column('confirm_password', css_class='col-6'),
            )
        )
        self.helper.add_input(Submit('Submit', 'submit'))

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean(*args, **kwargs)

        if not cleaned_data['password'] == cleaned_data['confirm_password']:
            raise forms.ValidationError('The passwords supplied do not match')

        if User.objects.filter(username=cleaned_data['username']):
            raise forms.ValidationError('That username is already taken')

        return cleaned_data
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = "user",

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'email',
            'date_of_birth',
            Row(
                Column('photo', css_class='col-6'),
                Column('bio', css_class='col-6'),
            )
        )
        self.helper.add_input(Submit('Submit', 'submit'))
