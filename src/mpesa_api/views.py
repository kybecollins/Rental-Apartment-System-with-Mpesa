from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.contrib.auth.decorators import login_required


@login_required
def getAccessToken(request):
    consumer_key = 'TQgOu4zrqA5zUhwauPwzDksMpAUuG8NT'
    consumer_secret = 'j2vbZTIp7VOCG2DA'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

    return HttpResponse(validated_mpesa_access_token)

@login_required
def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": request.POST['amount'],
        "PartyA": request.POST['phone_number'],  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": request.POST['phone_number'],  # replace with your phone number to get stk push
        "CallBackURL": "https://dd89-105-163-0-111.ngrok.io/api/v1/payment/lipaaa",
        "AccountReference": "USHUJAA RENTALS",
        "TransactionDesc": "Testing stk push"
    }

    response = requests.post(api_url, json=request, headers=headers)
    print(response.text)
    return HttpResponse('success')
    