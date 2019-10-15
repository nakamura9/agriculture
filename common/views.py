from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  UpdateView, 
                                  DetailView)

import os
from common.models import Profile
from common import forms
from common.utils import ContextMixin


class HomePage(TemplateView):
    template_name = os.path.join('common', 'home.html')

class CreateProfileView(ContextMixin, CreateView):
    form_class = forms.ProfileForm
    template_name = os.path.join('common', 'create_template.html')
    extra_context = {
        'title': "Profile",
        'description': "Create a profile to get the most out of the app's features"
    }

class UpdateProfileView(ContextMixin, UpdateView):
    form_class = forms.ProfileForm
    model = Profile
    template_name = os.path.join('common', 'create_template.html')
    extra_context = {
        'title': "Edit Profile",
        'description': "Make changes to your profile."
    }

class ProfileDetailView(DetailView):
    model = Profile
    template_name = os.path.join('common', 'profile_detail.html')
    