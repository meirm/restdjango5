from django.urls import path, include
from rest_framework.routers import DefaultRouter

from snippets import views


# The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]