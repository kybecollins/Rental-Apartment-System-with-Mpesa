from django.urls import path

from dashboards.views import(
    home_dashboard_view,
    payment_dashboard_view,
    settings_dashboard_view,
    edit_profile_view,
    mpesa_payment_dashboard_view,
    lipa_na_mpesa,
    receipt_dash_view
)


app_name='dashboards'

urlpatterns = [
    
    path('dmain/',home_dashboard_view,name='homedash'),
    path('payment/',payment_dashboard_view,name='payment'),
    path('mpayment/',mpesa_payment_dashboard_view,name='mpayment'),
    path('settings/',settings_dashboard_view,name='settings'),
    path('editprofile/',edit_profile_view,name='editprofile'),
    path('receipt/',receipt_dash_view,name='receipt'),
    # path('lipa_na_mpesa',lipa_na_mpesa,name='payed'),
    # path('pay/',lipa,name='payed'),


    

]