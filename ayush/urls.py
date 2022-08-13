from django.contrib import admin
from django.urls import path,include
from .views import Eventhandle,home,Editevent,Deleteevent
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('home',home,basename='home')
router.register('event',Eventhandle,basename='allevent')
router.register('updateevent',Editevent,basename='update')
router.register('deleteevent',Deleteevent,basename='delete')


urlpatterns = [
    path('',include(router.urls)),
]
