
from rest_framework.routers import path
from authentication.views import HomeView, LogoutView

urlpatterns = [
    path('home/', HomeView.as_view(), name ='home'),
    path('logout/', LogoutView.as_view(), name ='logout')
]

