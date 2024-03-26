"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter
import snippets.views as snippet_views
import prompts.views as prompt_views
import users.views as user_views
import authentication.views as views
router = DefaultRouter()
router.register(r'api/v1/snippets', snippet_views.SnippetViewSet, basename='snippet')
router.register(r'api/v1/users', user_views.UserViewSet, basename='user')
router.register(r'api/v1/prompts', prompt_views.PromptViewSet, basename='prompt')
router.register(r'api/v1/categories', prompt_views.CategoryViewSet, basename='category')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('authentication.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh'),
     
]

