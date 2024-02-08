from django.urls import path

from .views import HomaPageView, CreatePostView

urlpatterns = [
    path("", HomaPageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
]