
# import the classes we need to use in this file
import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

# create a class called MpesaC2BCredential.
class MpesaC2bCredential:
    consumer_key = 'bPou4CxYVDQA1MipV6GjkJI2q0XGoqB4' #create our consumer_key variable
    consumer_secret = 'u6xhCpX4Tlms5Qcw'  #create our consumer_secret variable
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials' #create a URL variable for generating the mpesa token

# create a class called MpesaAccessToken. This is the class we are going to use to make a call to mpesa.
class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']

# create a class called LipanaMpesaPassword
class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S') #define the format of our transaction timestamp where we start with the year, month, date, hour, minute and second.
    Business_short_code = "174379" #define our business Shortcode (Paybill no)
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919' #define our passkey, this is also given in Mpesa sandbox test credentials.

    #we define our password used to encrypt the request we send mpesa API STK push URL. The password is a base64 string which is a combination of Shortcode+Passkey+Timestamp.
    data_to_encode = Business_short_code + passkey + lipa_time
    print()
    #encode our password to base64 string
    online_password = base64.b64encode(data_to_encode.encode())
    #decode our password to UTF-8
    decode_password = online_password.decode('utf-8')