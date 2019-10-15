from django import forms
from common.models import Profile
from crispy_forms.layout import Layout, Row, Column, HTML, Submit
from crispy_forms.helper import FormHelper


class ProfileForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm = forms.CharField(widget=forms.PasswordInput)
    
    
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
