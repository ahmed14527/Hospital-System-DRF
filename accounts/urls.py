
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from .views import LogoutView

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),

]
