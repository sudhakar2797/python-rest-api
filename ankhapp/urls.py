"""phoenix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ankhapp import views

router=DefaultRouter()
router.register('welcome-viewset',views.WelcomeViewSet,basename='welcome-viewset')
router.register('welcome-modelviewset',views.UserProfileViewSet,basename='welcome-modelviewset')
router.register('taskdetails',views.TaskDetailsViewSet,basename='taskdetailsviewset')

urlpatterns = [
    path('get-hello/',views.WelcomeAPIView.as_view()),
    path('login/',views.CheckValidUser.as_view()),
    path('',include(router.urls))
]
