import json
import urllib2


def getBlock():
    try:
        data = urllib2.urlopen("https://chain.api.btc.com/v3/block/latest").read()
        response = json.loads(data)
        print "Latest Version::" + str(response['data']['size'])
        print "Hash::" + str(response['data']['hash'])
        print "Previous Block Hash::" + str(response['data']['prev_block_hash'])
        print "Size::" + str(response['data']['size'])
        print "Difficulty::" + str(response['data']['difficulty'])
        print "Created_at::" + str(response['data']['created_at'])
    except:
        print "Try Again"


def getBlockListByDate(d):
    try:
        url = "https://chain.api.btc.com/v3/block/date/"
        data = urllib2.urlopen(url + str(d)).read()
        response = json.loads(data)
        print "Hash::" + str(response['data'][0]['hash'])
        print "Previous Block Hash::" + str(response['data'][0]['prev_block_hash'])
        print "Next Block Hash::" + str(response['data'][0]['next_block_hash'])
        print "Hash::" + str(response['data'][1]['hash'])
        print "Previous Block Hash::" + str(response['data'][1]['prev_block_hash'])
        print "Next Block Hash::" + str(response['data'][1]['next_block_hash'])
    except:
        print "Try Again"


def getAddressInfo(address):
    try:
        url = "https://chain.api.btc.com/v3/address/"
        data = urllib2.urlopen(url + str(address)).read()
        response = json.loads(data)
        print "Address::" + str(response['data']['address'])
        bal = str(response['data']['balance'])
        if len(bal) < 8:
            print "Balance:: ." + str(response['data']['balance']) + " ""BTC"
        else:
            print "Balance:: " + str(response['data']['balance']) + " ""BTC"
        print "Total Transaction::" + str(response['data']['tx_count'])
    except:
        print "Try Again"
