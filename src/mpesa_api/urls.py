from django.urls import path,include
from mpesa_api import views



app_name='mpesa_api'
urlpatterns = [

    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesaaa'),
    path('payment/', include('mpesa_api.api.urls')),
]