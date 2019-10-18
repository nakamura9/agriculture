from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, HTML, Submit, Row, Column
from crispy_forms.bootstrap import Tab, TabHolder
from projects import models
from common.models import Profile
from django.contrib.auth.models import User 

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


class ActivityForm(forms.ModelForm):
    project = forms.ModelChoiceField(models.Project.objects.all(),
        widget=forms.HiddenInput)

    class Meta:
        exclude = "actual_cost", "completed_date",
        model = models.Activity

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='col-6'),
                Column('start_date', css_class='col-6'),
            ),
            'description',
            'estimated_cost',
            'project',
            'responsible',
        )
        self.helper.add_input(Submit('Submit', 'submit'))

class AgentForm(forms.ModelForm):
    class Meta: 
        exclude = 'profile',
        model = models.Agent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'full_name',
            'role',
            'profile'
        )
        self.helper.add_input(Submit('Submit', 'submit'))


class RoleForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'
        model = models.Role

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
        )
        self.helper.add_input(Submit('Submit', 'submit'))

class ActionForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'
        model = models.Action
        widgets = {
            'activity': forms.HiddenInput
        }
        labels = {
            'taken_by': 'Actor'
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'activity',
            'date',
            'taken_by',
            'description',
            'estimated_cost'
        )
        self.helper.add_input(Submit('Submit', 'submit'))

class MilestoneForm(forms.ModelForm):
    class Meta: 
        fields = 'date', 'name', 'description', 'target', 'activity'
        model = models.Milestone
        widgets = {
            'activity': forms.HiddenInput
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'date',
            'activity',
            'name',
            'description',
            'target',
        )
        self.helper.add_input(Submit('Submit', 'submit'))


class MilestoneReviewForm(forms.ModelForm):
    class Meta: 
        fields = '__all__'
        model = models.Milestone

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'review_date',
            'actual',
            'review_comments',
            'status',
        )
        self.helper.add_input(Submit('Submit', 'submit'))



class InputForm(forms.ModelForm):
    class Meta: 
        fields = "__all__"
        model = models.Input
        widgets = {
            'activity': forms.HiddenInput
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'description',
            'category',
            'activity',
            Row(
                Column('unit', css_class='col-4'),
                Column('unit_cost', css_class='col-4'),
                Column('quantity', css_class='col-4')
            )
        )
        self.helper.add_input(Submit('Submit', 'submit'))



class ExpenseForm(forms.ModelForm):
    class Meta: 
        fields = "__all__"
        model = models.Expense
        widgets = {
            'activity': forms.HiddenInput
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'date',
            'activity',
            'vendor',
            'description',
            'expense_category',
            'amount',
        )
        self.helper.add_input(Submit('Submit', 'submit'))


class ExpenseCategoryForm(forms.ModelForm):
    class Meta: 
        fields = "__all__"
        model = models.ExpenseCategory
       
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
        )
        self.helper.add_input(Submit('Submit', 'submit'))


class InputCategoryForm(forms.ModelForm):
    class Meta: 
        fields = "__all__"
        model = models.InputCategory
       
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'description',
        )
        self.helper.add_input(Submit('Submit', 'submit'))


class UnitForm(forms.ModelForm):
    class Meta: 
        fields = "__all__"
        model = models.UnitOfMeasure
       
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'symbol',
            'description',
        )
        self.helper.add_input(Submit('Submit', 'submit'))
