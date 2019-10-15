from django.urls import path
from common import views


urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
    path('create-profile/', views.CreateProfileView.as_view(), 
        name='create-profile'),
    path('update-profile/<int:pk>', views.UpdateProfileView.as_view(), 
        name='update-profile'),
    path('profile-details/<int:pk>', views.ProfileDetailView.as_view(), 
        name='profile-details'),
]
