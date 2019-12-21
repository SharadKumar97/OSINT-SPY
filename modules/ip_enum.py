import shodan
from modules.config import *
SHODAN_API_KEY=shodan_api_key
global api
api=shodan.Shodan(SHODAN_API_KEY)
def ipEnum(IP):
    try:
        print(IP)
        host=api.host(IP)
        print("Host :: "+str(host['ip_str']))
        print("Country Name :: "+str(host['country_name']))
        print("City :: "+str(host['city']))
        print("Organization :: "+str(host['org']))
        print("ISP :: "+str(host['isp']))
        print("Vulnerability CVE ID :: "+str(host['vulns']))
        print("Open ports :: "+str(host['ports']))
    except:
        print("Try Again")

