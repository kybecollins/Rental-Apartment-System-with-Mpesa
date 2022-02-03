from django.contrib.auth import get_user_model
User = get_user_model()


from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from mpesa_api.models import LNMOnline
from mpesa_api.api.serializers import LNMOnlineSerializer

class LNMCallbackUrlApiView( CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]


    def create (self,request):
        print(request.data,"this is request.data")

        merchant_request_id = request.data["Body"]["stkCallback"]["MerchantRequestID"]
        checkout_request_id = request.data["Body"]["stkCallback"]["CheckoutRequestID"]
        result_code = request.data["Body"]["stkCallback"]["ResultCode"]
        result_description = request.data["Body"]["stkCallback"]["ResultDesc"]
        amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0][
            "Value"
        ]
        mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][1]["Value"]
        balance = ""
        transactiondate = request.data["Body"]["stkCallback"]["CallbackMetadata"][
            "Item"
        ][3]["Value"]
        phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][
            4
        ]["Value"]

        

        from datetime import datetime
        str_tarnsaction_date = str(transactiondate)
        tranasction_datetime=datetime.strptime(str_tarnsaction_date,"%Y%m%d%H%M%S")
        print(tranasction_datetime)

        from mpesa_api.models import LNMOnline
        our_model = LNMOnline.objects.create(
            CheckoutRequestID =merchant_request_id,
            MerchantRequestID =checkout_request_id,
            ResultCode =result_code,
            ResultDesc =result_description,
            Amount=amount,
            MpesaReceiptNumber=mpesa_receipt_number,
            Balance =balance,
            TransactionDate=tranasction_datetime,
            PhoneNumber=phone_number,


        )
        our_model.save()