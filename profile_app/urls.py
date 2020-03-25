
from django.urls import path,include
from .views import HelloApiView,UserViewSet,UserLoginApi,UserProfileFeedViewset 
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('hello_api_viewset', UserViewSet, basename='viewset')
router.register('profiles',UserProfileFeedViewset)


urlpatterns = [
    path('hello_api_view/', HelloApiView.as_view()),
    path('login/', UserLoginApi.as_view()),
    path('',include(router.urls))
]



