from .config import *
from .utils import format_dict
import clearbit
import requests
clearbit.key = clearbit_api_key


def get_company_detail(domain, json_output=False):
    try:
        company = clearbit.Company.find(domain=domain, stream=True)
    except Exception as e:
        print(e)
    else:
        company_details = None
        if company is not None:
            if json_output:
                company_details = dict(company)
            else:
                format_dict(company)

        # Extracting emails
        url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={email_hunter_api_key}'
        response = requests.get(url)
        json_response = response.json()
        if json_output:
            if response.ok:
                company_details['Extracted Emails'] = json_response
            else:
                company_details['Error for Email Extraction'] = json_response
            print(company_details)
        else:
            if response.ok:
                emails_list = json_response['data']['emails']
                if emails_list:
                    print("\nExtracted Emails:: ")
                    for email in emails_list:
                        print(email['value'])
            else:
                print("\nError while extracting emails using email_hunter_api_key::")
                print(f"Error Description:: {json_response['errors'][0]['details']}.")
