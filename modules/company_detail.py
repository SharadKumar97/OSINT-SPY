from modules.config import *
import requests
import json
import clearbit
clearbit.key=clearbit_api_key
def getDetail(domain):
    try:
        company=clearbit.Company.find(domain=domain,stream=True)
        if company != None:
            print("Domain Name :: "+str(company['domain']))
            print("Description :: "+str(company['description']))
            print("Location :: "+str(company['location']))
            print("EmailAddress :: "+str(company['site']['emailAddresses']))
            print("Number of Employees :: "+str(company['metrics']['employees']))
            print("Contact Number :: "+str(company['phone']))
            print("\n")
            print("Extracted Emails :: ")
            url="https://api.hunter.io/v2/domain-search?domain="+domain+"&api_key="+email_hunter_api_key
            emails=requests.get(url)
            parsed_emails=json.loads(emails.text)
            for email in parsed_emails['data']['emails']:
                print(email['value'])
        else:
            print("No information")
    except:
        print("Try Again")

