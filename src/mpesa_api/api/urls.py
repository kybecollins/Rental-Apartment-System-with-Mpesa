from django.urls import path,include
from django.views.generic.base import View
from mpesa_api import views

from mpesa_api.api.views import LNMCallbackUrlApiView


urlpatterns = [

    path('lipaaa', LNMCallbackUrlApiView.as_view() , name='lnm-callbackurl'),
   
]