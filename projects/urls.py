from django.urls import path
from projects import views


urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create-project/', views.ProjectCreateView.as_view(), 
        name='create-project'),
    path('project-details/<int:pk>/', views.ProjectDetailView.as_view(), 
        name='project-details'),
    path('update-project/<int:pk>/', views.ProjectUpdateView.as_view(), 
        name='update-project'),
    path('create-activity/<int:project>', views.ActivityCreateView.as_view(), 
        name='create-activity'),
    path('activity-details/<int:pk>/', views.ActivityDetailView.as_view(), 
        name='activity-details'),
    path('update-activity/<int:pk>/', views.ActivityUpdateView.as_view(), 
        name='update-activity'),
    path('create-agent/<int:project>', views.AddAgent.as_view(), 
        name='create-agent'),
    path('agent-details/<int:pk>/', views.AgentDetails.as_view(), 
        name='agent-details'),
    path('update-agent/<int:pk>/', views.UpdateAgent.as_view(), 
        name='update-agent'),
    path('create-role/', views.CreateRole.as_view(), 
        name='create-role'),
    path('create-milestone/<int:activity>/', views.CreateMilestone.as_view(), 
        name='create-milestone'),
    path('review-milestone/<int:pk>/', views.ReviewMilestone.as_view(), 
        name='review-milestone'),
    path('create-action/<int:activity>/', views.CreateAction.as_view(), 
        name='create-action'),
    path('milestone-details/<int:pk>/', views.MilestoneDetails.as_view(), 
        name='milestone-details'),
    path('action-details/<int:pk>/', views.ActionDetails.as_view(), 
        name='action-details'),
    path('create-input/<int:activity>/', views.CreateInput.as_view(), 
        name='create-input'),
    path('create-expense/<int:activity>/', views.CreateExpense.as_view(), 
        name='create-expense'),
    path('create-input-category/', views.CreateInputCategory.as_view(), 
        name='create-input-category'),
    path('create-expense-category/', views.CreateExpenseCategory.as_view(), 
        name='create-expense-category'),
    path('create-unit/', views.CreateUnit.as_view(), 
        name='create-unit'),
]
