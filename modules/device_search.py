from .config import *
import shodan
import time


def get_device(device_name, json_output=False):
    try:
        api = shodan.Shodan(shodan_api_key)
        results = api.search(device_name)
        time.sleep(5)
        if json_output:
            print(results)
            return
        print(f"Results Found: {results['total']}")
        for result in results['matches']:
            print(f"Ip:: {result['ip_str']} | Organization:: {result['org']} |"
                  f" Domain:: {result['domains']} | ISP:: {result['isp']}")

    except shodan.APIError as e:
        print(e)
