import requests
from requests.models import Response

from datetime import datetime
import base64
from requests.auth import HTTPBasicAuth



def lipa_na_mpesa(phonenumber,amounts):
    phone_number = phonenumber
    amount = amounts

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
    