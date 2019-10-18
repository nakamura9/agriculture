from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  DetailView, 
                                  UpdateView)
import os 
from projects import models
from projects import forms
from common.utils import ContextMixin

CREATE_TEMPLATE = os.path.join("common", "create_template.html")
MODAL_TEMPLATE  = os.path.join('common', 'modal_template.html')


class DashboardView(TemplateView):
    template_name = os.path.join("projects", "dashboard.html")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.filter(owner=self.request.user.profile)
        return context

class ProjectCreateView(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.ProjectForm
    extra_context = {
        'title': "New Project",
        'description': "Start a new Farming Project"
    }

    def get_initial(self):
        return {
            'owner': self.request.user.profile
        }


class ProjectUpdateView(ContextMixin, UpdateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.ProjectForm
    model = models.Project
    extra_context = {
        'title': "Edit Project",
        'description': "Make changes to an existing project"
    }



class ProjectDetailView(DetailView):
    template_name =os.path.join('projects', 'project', 'detail.html')
    model = models.Project

class ActivityCreateView(ContextMixin, CreateView):
    form_class = forms.ActivityForm
    template_name = CREATE_TEMPLATE
    extra_context = {
        'title': "New Project Stage",
        'description': "Outline the different stages that will be required to complete your project."
    }

    def get_initial(self):
        return {
            'project': self.kwargs['project']
        }

class ActivityUpdateView(ContextMixin, UpdateView):
    form_class = forms.ActivityForm
    template_name = CREATE_TEMPLATE
    model = models.Activity
    extra_context = {
        'title': "Edit Activity",
        'description': "Make changes to an activity."
    }


class ActivityDetailView(DetailView):
    template_name = os.path.join('projects', 'activity', 'detail.html')
    model = models.Activity

class AddAgent(ContextMixin, CreateView):
    template_name = os.path.join('common', 'modal_template.html')
    form_class = forms.AgentForm
    extra_context ={
        'title': 'Add Agent'
    }
    success_url = "/home/"


class UpdateAgent(ContextMixin, UpdateView):
    template_name = os.path.join('common', 'modal_template.html')
    form_class = forms.AgentForm
    extra_context ={
        'title': 'Add Agent'
    }
    success_url = "/home/"


class AgentDetails(ContextMixin, DetailView):
    template_name = os.path.join('projects', 'agent', 'detail.html')
    #agents have limited access to the site via a portal and can update the project via actions.


class CreateRole(ContextMixin, CreateView):
    template_name = os.path.join('common', 'modal_template.html')
    form_class = forms.RoleForm
    extra_context = {
        'title': 'Add Role'
    }
    success_url = "/home/"

class CreateMilestone(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.MilestoneForm
    extra_context = {
        'title': 'Set a milestone for a stage in your project'
    }

    def get_initial(self):
        return {
            'activity': self.kwargs['activity']
        }

class ReviewMilestone(ContextMixin, UpdateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.MilestoneForm
    model = models.Milestone
    extra_context = {
        'title': 'Review progress made towards a milestone'
    }


class CreateAction(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.ActionForm
    extra_context = {
        'title': 'Record an action undertaken on behalf of your project'
    }

    def get_initial(self):
        return {
            'activity': self.kwargs['activity']
        }

class MilestoneDetails(DetailView):
    template_name = os.path.join('projects', 'milestone', 'details.html')
    model = models.Milestone

class ActionDetails(DetailView):
    template_name = os.path.join('projects', 'action', 'details.html')
    model = models.Action


class CreateInput(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.InputForm
    extra_context = {
        'title': 'Create Input',
        'description': 'Use this form in the planning stage to identify resources required to complete the current project stage'
    }
    success_url = "/home/"


    def get_initial(self):
        return {
            'activity': self.kwargs['activity']
        }


class CreateExpense(ContextMixin, CreateView):
    template_name = CREATE_TEMPLATE
    form_class = forms.ExpenseForm
    extra_context = {
        'title': 'Create Expense',
        'description': 'Record costs incurred during the current project stage'
    }
    success_url = "/home/"


    def get_initial(self):
        return {
            'activity': self.kwargs['activity']
        }
    


class CreateInputCategory(ContextMixin, CreateView):
    template_name = MODAL_TEMPLATE
    form_class = forms.InputCategoryForm
    extra_context = {
        'title': 'Create Input Category',
    }
    success_url = "/home/"

class CreateExpenseCategory(ContextMixin, CreateView):
    template_name = MODAL_TEMPLATE
    form_class = forms.ExpenseCategoryForm
    extra_context = {
        'title': 'Create Expense Category',
    }
    success_url = "/home/"


class CreateUnit(ContextMixin, CreateView):
    template_name = MODAL_TEMPLATE
    form_class = forms.UnitForm
    extra_context = {
        'title': 'Create Unit',
    }
    success_url = "/home/"
