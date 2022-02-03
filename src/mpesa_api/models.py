from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class LNMOnline(models.Model):
    tenant = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    CheckoutRequestID =models.CharField(max_length= 50, blank=True,null = True)
    MerchantRequestID = models.CharField(max_length=30, blank=True,null = True)
    ResultCode = models.IntegerField( blank=True,null = True)
    ResultDesc = models.CharField(max_length=50, blank=True,null = True)
    Amount =models.FloatField(blank=True,null = True )
    MpesaReceiptNumber=models.CharField(max_length=15, blank=True,null = True)
    Balance =models.CharField(max_length=12, blank=True,null = True)
    TransactionDate=models.DateField(blank=True,null = True)
    PhoneNumber=models.CharField(max_length=13, blank=True,null = True)    
