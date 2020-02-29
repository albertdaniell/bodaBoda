import datetime
import base64
import json
import time
import requests
from requests.auth import HTTPBasicAuth


"""
# from . access_tk import access_tk as access_tk

"""
#print(datetime.datetime.now())

# get access token


businessShortCode="174379" #lipa na mpesa short code
partA='254791836987'
partB=businessShortCode
ConsumerKey='I7qtM5EaaF50VJr4Rn3BJQ7vHAwnsdpx'
ConsumerSecret='UWfpwANAfGMMHL2v'
lipa_na_mpesa_passkey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
shortcode1='601360'


# time.sleep(2)

def generateToken():
    consumer_key = ConsumerKey
    consumer_secret =ConsumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_res=r.json()
    myaccess_token=json_res['access_token']
    print(myaccess_token)
    return myaccess_token




# End get of access token




unformated_time=datetime.datetime.now()
formatted_time=unformated_time.strftime("%Y%m%d%H%M%S")

#print(formatted_time)

#generating a time stamp

#base 64



data_to_encode=businessShortCode + lipa_na_mpesa_passkey + formatted_time
encoded_string=base64.b64encode(data_to_encode.encode())

decoded_pass=encoded_string.decode('utf8')

#print (decoded_pass)




#print(myaccess_token)

    #print (r.json())


def lipa_na_mpesa(phone_no='254791836987',amount=20,payBill=businessShortCode,accref='Wasafi crocs'):
    print("making payments")
    myaccess_token=generateToken()

    print("generated access token {}".format(myaccess_token))
    access_token = myaccess_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = { "Authorization": "Bearer %s" % access_token }
    print("Passed the api url line")
    
    request = {
    "BusinessShortCode": payBill,
    "Password": decoded_pass,
    "Timestamp":formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": amount,
    "PartyA": phone_no,
    "PartyB":partB,  
    "PhoneNumber": phone_no,  
    "CallBackURL": "http://134.209.148.107/lnmpOnline/",  
    "AccountReference": accref,
    "TransactionDesc": "fee payment"
    }

    
    print("About to get the response")

    response = requests.post(api_url, json = request, headers=headers)

    # print ("This is the response",response.text)
    parsed_data = json.loads(response.text)
    print (response.text)
    # print ("The response code =",parsed_data['ResponseCode'])
    ResponseCode=parsed_data['ResponseCode']
    print("The response code is {}".format(ResponseCode))
    return ResponseCode

"""

{'Body': {'stkCallback': {'MerchantRequestID': '23481-4888433-1', 'CheckoutRequestID': 'ws_CO_DMZ_384585971_04072019121246169', 'ResultCode': 0, 'ResultDesc': 'The service request is processed successfully.', 'CallbackMetadata': {'Item': [{'Name': 'Amount', 'Value': 1.0}, {'Name': 'MpesaReceiptNumber', 'Value': 'NG421NVTR6'}, {'Name': 'Balance'}, {'Name': 'TransactionDate', 'Value': 20190704121251}, {'Name': 'PhoneNumber', 'Value': 254791836987}]}}}} 

"""



# generateToken()
# lipa_na_mpesa()