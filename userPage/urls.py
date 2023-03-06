from django.urls import path
from .views import ShowProfilePageView, CreateProfilePageView, EditProfilePageView

urlpatterns = [
    path('<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),
    path('create_profile_page/',CreateProfilePageView.as_view(), name='create_user_profile'),
    path('<int:pk>/settings/',EditProfilePageView.as_view(), name='edit_user_profile'),
]