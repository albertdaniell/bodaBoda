from requests.auth import HTTPBasicAuth
import requests

businessShortCode="174379" #lipa na mpesa short code
partA='254791836987'
partB=businessShortCode
ConsumerKey='I7qtM5EaaF50VJr4Rn3BJQ7vHAwnsdpx'
ConsumerSecret='UWfpwANAfGMMHL2v'
lipa_na_mpesa_passkey='bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
shortcode1='601360'

def generateToken():
    consumer_key = ConsumerKey
    consumer_secret =ConsumerSecret
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    json_res=r.json()
    myaccess_token=json_res['access_token']
    print(myaccess_token)
    return myaccess_token


generateToken()