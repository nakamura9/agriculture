from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Submit, Row, Column
from crispy_forms.bootstrap import Tab, TabHolder
from projects import models
from common.models import Profile

class ProjectForm(forms.ModelForm):
    owner = forms.ModelChoiceField(Profile.objects.all(),
        widget=forms.HiddenInput)

    class Meta:
        fields = "__all__"
        model = models.Project

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-6'),
                Column('type', css_class='col-6'),
            ),
            'description',
            'owner',
            'start_date',
        )
        self.helper.add_input(Submit('Submit', 'submit'))

        