from rest_framework import routers
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

from django.urls import path, include

# router = routers.DefaultRouter()
# router.register('api/user', UserAPI,'user')
# router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth/login', LoginAPI.as_view()),
    path('api/auth/user', UserAPI.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(),
    name='knox_logout'),
]


# urlpatterns += router.urls