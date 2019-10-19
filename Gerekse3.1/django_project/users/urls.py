from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django_project.views import anasayfa
from blog import views as blog_views
from .views import (
    ProfileDetailView,
)

urlpatterns = [
    path('', user_views.profile, name="profile"),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)