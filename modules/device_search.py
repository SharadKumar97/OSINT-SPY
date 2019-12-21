import shodan
import time
from modules.config import *
SHODAN_API_KEY=shodan_api_key
api=shodan.Shodan(SHODAN_API_KEY)
def getDevice(device_name):
    try:
        results=api.search(device_name)
        time.sleep(5)
        print("Results Found: %s" %results['total'])
        for result in results['matches']:
            print("Ip:%s"%result['ip_str']+"  | Organization: %s" %result['org']+ " | Domain:%s" %result['domains']+" | ISP :%s "%result['isp'])

    except:
        print('Failed.')

