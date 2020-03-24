
from django.urls import path,include
from .views import HelloApiView
from .views import UserViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('hello_api_viewset', UserViewSet, basename='viewset')


urlpatterns = [
    path('hello_api_view/', HelloApiView.as_view()),
    path('',include(router.urls))
]



