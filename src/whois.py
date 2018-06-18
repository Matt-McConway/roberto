import requests
import os
import json

WHO_IS_API_KEY = os.environ.get('WHO_IS_KEY')

"""
    https://jsonwhois.io
"""

class Who():
    def getWhois(self, domain, tld):
        if tld == "nz":
            return "I can't lookup .nz domains :'( "
        response = requests.get(
            "https://api.jsonwhois.io/whois/domain?key={}&domain={}.{}".format(WHO_IS_API_KEY, domain, tld)).json()


        if response["result"]["registered"]:
            expiry = response["result"]["expires"]
            nameserver = str(response["result"]["nameservers"])
            admin_name = response["result"]["contacts"]["admin"][0]["name"]
            admin_email = response["result"]["contacts"]["admin"][0]["email"]
            admin_city = response["result"]["contacts"]["admin"][0]["city"]
            admin_state = response["result"]["contacts"]["admin"][0]["state"]
            admin_country = response["result"]["contacts"]["admin"][0]["country"]
            registrar = response["result"]["registrar"]

            return "The domain {}.{} is registered! :(\n\
                    It will expire {}. \n\
                    The name servers are {}. \n\
                    Contact details: \n\
                    \tName: {}\n\
                    \tEmail: mailto:{}\n\
                    \tCity: {}\n\
                    \tState: {}\n\
                    \tCountry: {}\n\
                    And finally, the registrar: {}".format(domain, tld, expiry, nameserver, admin_name, admin_email, admin_city, admin_state, admin_country, registrar)
        else:
            return "The whois for {}.{} is unavailable.".format(domain, tld)

    def getRegistration(self, domain, tld):
        response = requests.get(
            "https://api.jsonwhois.io/whois/domain?key={}&domain={}.{}".format(WHO_IS_API_KEY, domain, tld)).json()
        if response["result"]["created"] is not None:
            return "{}.{} is registered :(".format(domain, tld)
        else:
            return "{}.{} is available!\n\
            Register now! - http://mer.nz/register".format(domain, tld)
