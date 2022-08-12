from django.contrib import admin
from django.urls import path,include
from .views import Eventhandle,home,Editevent,Deleteevent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('event/',Eventhandle.as_view(),name='allevent'),
    path('event/<str:category>',Eventhandle.as_view(),name='partevent'),
    path('updateevent',Editevent.as_view(),name='update'),
    path('updateevent/<int:id>',Editevent.as_view(),name='updateid'),
    path('deleteevent',Deleteevent.as_view(),name='delete'),
    path('deleteevent/<int:id>',Deleteevent.as_view(),name='deleteid')
    
]
