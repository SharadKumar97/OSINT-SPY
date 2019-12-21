import requests
import json

def getBlock():
    try:
        try:
            data=requests.get('https://chain.api.btc.com/v3/block/latest')
        except:
            print("Unable to fetch data! Check your internet connection.")
        if data.status_code == 200:
            response=data.json()
        try:
            print("Latest version::"+str(response['data']['size']))
            print("Hash::"+str(response['data']['hash']))
            print("Previous Block Hash::" + str(response['data']['prev_block_hash']))
            print("Size::" + str(response['data']['size']))
            print("Difficulty::" + str(response['data']['difficulty']))
            print("Created_at::" + str(response['data']['created_at']))
        except:
            print("Error while parsing response.")
    except:
        print('Try again')

def getBlockListByDate(d):
    try:
        try:
            data=requests.get('https://chain.api.btc.com/v3/block/date/'+str(d))
        except:
            print("Unable to fetch data! Check your internet connection.")
        if data.status_code == 200:
            response=data.json()
        try:
            print("Hash::" + str(response['data'][0]['hash']))
            print("Previous Block Hash::" + str(response['data'][0]['prev_block_hash']))
            print("Next Block Hash::" + str(response['data'][0]['next_block_hash']))
            print("Hash::" + str(response['data'][1]['hash']))
            print("Previous Block Hash::" + str(response['data'][1]['prev_block_hash']))
            print("Next Block Hash::" + str(response['data'][1]['next_block_hash']))
        except:
            print("Error while parsing response.")
    except:
        print('Try again')


def getAddressInfo(address):
    try:
        try:
            data=requests.get('https://chain.api.btc.com/v3/address/'+str(address))
        except:
            print("Unable to fetch data! Check your internet connection.")
        if data.status_code == 200:
            response=data.json()
        try:
            print("Address::" + str(response['data']['address']))
            print("Balance:: ." + str(response['data']['balance']) + " ""BTC")
        except:
            print("Error while parsing response.")
    except:
        print('Try again')
