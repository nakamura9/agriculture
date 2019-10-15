from django.urls import path
from projects import views


urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create-project/', views.ProjectCreateView.as_view(), 
        name='create-project'),
    path('project-details/<int:pk>/', views.ProjectDetailView.as_view(), 
        name='project-details')
]
