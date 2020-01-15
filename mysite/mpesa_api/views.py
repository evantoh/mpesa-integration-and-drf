
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
# import our MpesaAccessToken and LipanaMpesaPpassword classes from mpesa_credentials.py file
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
def getAccessToken(request):
	consumer_key = 'bPou4CxYVDQA1MipV6GjkJI2q0XGoqB4'
	consumer_secret = 'u6xhCpX4Tlms5Qcw'
	api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
	r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
	mpesa_access_token = json.loads(r.text)
	print("access token",mpesa_access_token)
	validated_mpesa_access_token = mpesa_access_token['access_token']
	return HttpResponse(validated_mpesa_access_token)


# define our STK push method called lipa_na_mpesa_online
def lipa_na_mpesa_online(request):
	access_token = MpesaAccessToken.validated_mpesa_access_token #get our mpesa access token.
	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest" #define our STK push URL provided by Safaricom.
	headers = {"Authorization": "Bearer %s" % access_token} #define our headers where we pass our access token

	#define our STK push parameters
	request = {
	"BusinessShortCode": LipanaMpesaPpassword.Business_short_code,#pass our mpesa Shortcode
	"Password": LipanaMpesaPpassword.decode_password, #pass our mpesa password.
	"Timestamp": LipanaMpesaPpassword.lipa_time, #define the transaction timestamp.
	"TransactionType": "CustomerPayBillOnline",#define the transaction type. Since it’s STK push we use CustomerPayBillOnline
	"Amount": 1200,#define the amount, in this case, one shilling.
	"PartyA": 254711536639,  # define the phone number sending the money.
	"PartyB": LipanaMpesaPpassword.Business_short_code,#define the organization shortcode receiving the funds.
	"PhoneNumber": 254711536639,  # define the mobile number to receive STK pin prompt.
	"CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/", #define a valid URL which will receive notification from Mpesa-api. Note this should be your confirmation URL
	"AccountReference": "Evans",#define an identifier of the transaction
	"TransactionDesc": "Testing stk push"# define the description of what the transaction is all about.
	}

	response = requests.post(api_url, json=request, headers=headers)#get the response from Safaricom mpesa api.
	return HttpResponse('success')# define a response
