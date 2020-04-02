from .utils import format_dict
import requests


def get_bitcoin_data(url, json_output=False):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Unable to fetch data! Check your internet connection.")
    except Exception as e:
        print(e)
    else:
        if response.status_code != 200:
            print('Server Side Error or Forbidden Access.\nTry after some time.')
            return

        response = response.json()
        if json_output:
            print(response)
            return
        if response['err_no'] == 0:
            data = response['data']
            if data:
                if isinstance(data, list):
                    for item in data:
                        format_dict(item)
                        print()
                else:
                    format_dict(data)
            else:
                print('No related information found.')

        else:
            print(f"Error Number:: {response['err_no']}")
            print(f"Error Message:: {response['err_msg']}")
