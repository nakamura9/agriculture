from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DetailView
import os 
from projects import models
from projects import forms
from common.utils import ContextMixin

class DashboardView(TemplateView):
    template_name = os.path.join("projects", "dashboard.html")

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['projects'] = models.Project.objects.all()
        return context

class ProjectCreateView(ContextMixin, CreateView):
    template_name = os.path.join('common', 'create_template.html')
    form_class = forms.ProjectForm
    extra_context = {
        'title': "New Project",
        'description': "Start a new Farming Project"
    }

    def get_initial(self):
        return {
            'owner': None
        }


class ProjectDetailView(DetailView):
    template_name =os.path.join('projects', 'project', 'detail.html')
    model = models.Project

