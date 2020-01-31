from .config import *
from .utils import format_dict
import shodan


def ip_details(ip, json_output=False):
    try:
        api = shodan.Shodan(shodan_api_key)
        host = api.host(ip)
        if json_output:
            print(host)
            return
        print(f'IP Provided:: {ip}')
        format_dict(host, attribute='data')
    except shodan.APIError as e:
        print(e)
