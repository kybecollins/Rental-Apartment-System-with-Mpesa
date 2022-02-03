"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from officials.views import default_home_view,default_apartment_view,default_about_view, default_contact_view
# from accounts.views import home_view
# from accounts.views import logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('dashboards/',include('dashboards.urls')),
    path('chats/',include('chat.urls')),
    path('',default_home_view,name='home'),
    
    path('apartment/',default_apartment_view,name='apartmentpic'),
    path('about/',default_about_view,name='about'),
    path('contact/',default_contact_view,name='contact'),

    # path('logout/',logout_view,name='logout')
    # path('dmain/',home_dashboard_view,name='homedash')

    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include('mpesa_api.urls')),
    # path('api/payment/', include('mpesa_api.api.urls')),
    
]

urlpatterns += staticfiles_urlpatterns()



