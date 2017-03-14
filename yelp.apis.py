"""
App ID
0YjNsvpE94UBbDvKi3ziyw
App Secret
uFGtTRqqdszyv0STprpoT5k151MK3gJKdfjAG0JtiyIFZA67avsL2WMuT0SVHuHZ
"""

# import urllib2 
# from urllib2 import urlopen()
# from json import load
# import rauth
# from rauth import OAuth1Service

# yelp_api = "PKGgx6DiZBTF3ogmxqVjuq2dRD9QbC6V"




from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key="9ya3EmVmecA59vFDW-pgkg",
    consumer_secret="hAITWI30mXd6uAAHY11tZO44b-o",
    token="9b-bz8GbdWQOV9gQeXcwJ_gLgSaRrluM",
    token_secret="KSHMtAc8NuyA3Bc4lLUM3mAm8tE"
)

client = Client(auth)

# params = {
#     'term': 'food',
#     'lang': 'fr'
# }

# client.search('San Francisco', **params)

params = {
    'lang': 'fr'
}

client.get_business('yelp-san-francisco', **params)




results = client.search('San Francisco', **params)
print results.businesses

for businesses in results():
        print businesses ("name ") + item("phone")


# def get_search_parameters(lat,long):
#     #See the Yelp API for more details
#     params = {}
#     params["term"] = "restaurant"
#     params["ll"] = "{},{}".format(str(lat),str(long))
#     params["radius_filter"] = "2000"
#     params["limit"] = "10"
#     return params


# def get_results(params):
#     #Obtain these from Yelp's manage access page
#     consumer_key="9ya3EmVmecA59vFDW-pgkg",
#     consumer_secret="hAITWI30mXd6uAAHY11tZO44b-o",
#     token="9b-bz8GbdWQOV9gQeXcwJ_gLgSaRrluM",
#     token_secret="KSHMtAc8NuyA3Bc4lLUM3mAm8tE"

   
#     session = rauth.OAuth1Session(
#         consumer_key = "9ya3EmVmecA59vFDW-pgkg",
#         consumer_secret = "hAITWI30mXd6uAAHY11tZO44b-o",
#         access_token = "9b-bz8GbdWQOV9gQeXcwJ_gLgSaRrluM",
#         access_token_secret = "KSHMtAc8NuyA3Bc4lLUM3mAm8tE"
     
#     request = session.get("http://api.yelp.com/v2/search",params=params)
   
#     #Transforms the JSON API response into a Python dictionary
#     data = request.json()
#     session.close()
   
#     return data


# def main():
#     locations = [(39.98,-82.98),(42.24,-83.61),(41.33,-89.13)]
#     api_calls = []
#     for lat,long in locations:
#         params = get_search_parameters(lat,long)
#         api_calls.append(get_results(params))
#         print get_results(params)
#         #Be a good internet citizen and rate-limit yourself
#         #time.sleep(1.0)

# main()
