from django.shortcuts import render , redirect
from dashboards.forms import EditProfileForm
from dashboards.lipa import lipa_na_mpesa

from django.conf import settings
User = settings.AUTH_USER_MODEL

import requests
from requests.models import Response
from mpesa_api.models import LNMOnline

from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth


# Create your views here.
def home_dashboard_view(request):
    context= {}
    return render(request,'dashboards/dmain.html',context)

def payment_dashboard_view(request):
    context= {}
    return render(request,'dashboards/payment.html',context)

def settings_dashboard_view(request):
    context= {}
    return render(request,'dashboards/settings.html',context)

def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance = request.user)

        if form.is_valid():
            form.save()
            return render(request,'dashboards/editprofile.html') 
        
    else:
        form =EditProfileForm(instance =request.user)
        context ={'form':form}
        return render(request,'dashboards/editprofile.html',context) 

def mpesa_payment_dashboard_view(request):
     context= {}
     return render(request,'dashboards/payment2.html',context)

def receipt_dash_view(request):
    
    receipts= LNMOnline.objects.filter(tenant=request.user)
    context = {'receipts': receipts}
    return render(request,'dashboards/receipts.html',context)


# def lipa(request):
#     phone=request.POST['phone_number']
#     money=request.POST['amount']
#     lipa_na_mpesa(phone,money)
#     context= {}
#     return render(request,'dashboards/payment2.html',context)


def lipa_na_mpesa(request):
    phone_number = request.POST['phone_number']
    amount = request.POST['amount']

    BusinessShortCode = "174379"
    lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    consumer_key= 'TQgOu4zrqA5zUhwauPwzDksMpAUuG8NT'
    consumer_secret= "j2vbZTIp7VOCG2DA"
    unformatted_time =datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    data_to_encode = BusinessShortCode + lipa_na_mpesa_passkey + formatted_time
    encoded = base64.b64encode(data_to_encode.encode())

    decoded = encoded.decode('utf-8')

    consumer_key = consumer_key
    consumer_secret = consumer_secret
    api_URL = (
        "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    )
    r = requests.get(api_URL,auth=HTTPBasicAuth(consumer_key,consumer_secret))
    # print(r.text)
    json_response = r.json()
    my_access_token = json_response['access_token']
  
    access_token =my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    headers = {'Authorization': 'Bearer %s' % access_token }
    request = {
        "BusinessShortCode": "174379",
        "Password": decoded,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": "174379",
        "PhoneNumber": phone_number,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "36478120",
        "TransactionDesc": "Payment of Rent" 
    }
    response =requests.post(api_url,json=request,headers=headers)
    print(response.text)
    context= {}
    return render(request,'dashboards/calbak.html',context)

     # response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    # print(response.text.encode('utf8'))



    