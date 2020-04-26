from zeep import Client

"""
Special thanks to this YouTube Tutorial:
https://www.youtube.com/watch?v=JBYEQjg_znI

most helpful part was the following command:
$ python -mzeep [wsdl-adress]
Scroll down to Service: and you find all Operations
"""

# setting up the wsdl
client = Client(wsdl="http://ec.europa.eu/taxation_customs/vies/"
                "checkVatService.wsdl")

# fill the check list with dicts of country Code and VAT Number
vat_ids = [{"countryCode": "DE", "vatNumber": "295874949"},
           {"countryCode": "ATU", "vatNumber": "14662505"}]
# create the empty response list
response = []

# loop through the VAT-IDs
for id in vat_ids:
    try:
        r = client.service.checkVat(id["countryCode"], id["vatNumber"])
    except Exception as e:
        r = e
    finally:
        # append the responses to the response list
        response.append(r)

print(response)
