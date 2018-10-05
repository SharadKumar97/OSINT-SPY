from modules import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--btc_block", help="Find information regarding latest block of bitcoin", action="store_true")
parser.add_argument("--btc_date", help="Find out block information by date", type=int)
parser.add_argument("--btc_address", help="Find out bitcoin address information.")
parser.add_argument("--ssl_cipher", help="Find out what kind of ciphers are being used by server")
parser.add_argument("--ssl_bleed", help="Check whether server is vulnerable to heart bleed or not")
parser.add_argument("--domain", help="Find out basic detail of particular company through its domain name")
parser.add_argument("--email", help="Gather information from email address.")
parser.add_argument("--device", help="Find out devices which are connected to the internet.")
parser.add_argument("--ip", help="Enumerate information from IP Address.")
parser.add_argument("--skype_db", help="Use to find skype information.")
parser.add_argument("--malware", help="Find out whether a particular file is  infected with malware or not.")
parser.add_argument("--carrier", help="Give path of carrier file which will contain our text.")
parser.add_argument("--stego_text", help="Enter text to hide.")
parser.add_argument("--stego_find", help="Give path of image which contains hidden text.")
args = parser.parse_args()
if args.skype_db:
    global db_path
    db_path = args.skype_db
    getEmails(db_path)
    getContacts(db_path)
    getChat(db_path)

if args.btc_block:
    getBlock()
    exit()
if args.btc_date:
    d = args.btc_date
    getBlockListByDate(d)
    exit()
if args.btc_address:
    address = args.btc_address
    getAddressInfo(address)
    exit()
if args.ssl_cipher:
    server = args.ssl_cipher
    getCiphers(server)
    exit()

if args.ssl_bleed:
    server = args.ssl_bleed
    heartBleed(server)
    exit()
if args.domain:
    domain = args.domain
    getDetail(domain)
    heartBleed(domain)
    exit()
if args.email:
    email_id = args.email
    fetchData(email_id)
    exit()
if args.device:
    device_name = args.device
    getDevice(device_name)
    exit()
if args.ip:
    IP = args.ip
    ipEnum(IP)
    exit()
if args.malware:
    mal_name = args.malware
    sendMalware(mal_name)
    exit()
if args.carrier:
    carrier_path = args.carrier
if args.stego_text:
    secret_text = args.stego_text
    hideText(carrier_path, secret_text)
    exit()
if args.stego_find:
    steg_img = args.stego_find
    findText(steg_img)
    exit()


def printOnStart():
    print """

        
   @@@@@@@@@     @@@@@@@@@  |  @@      @  88888|88888       @@@@@@@@@  8@@@@@@@@  8           @
  88888888888    |          |  @ @     @       |            |          8       @    8        @
  @@@@@@@@@@@    |          |  @  @    @       |            |          8       @      8     @
  88888888888    |@@@@@@@@  |  @   @   @       |      ----  |@@@@@@@@  8@@@@@@@@        8  @
  @@@@@@@@@@@            |  |  @    @  @       |                    |  8                  @
  @@@@@@@@@@@            |  |  @     @ @       |                    |  8                 @
   888888888     @@@@@@@@|  |  @      @@       |            @@@@@@@@|  8                @
                    

                                     Search using OSINT
                                  Website: www.osint-spy.com
    
    Usage: osint-spy.py [options]
    Options:
    -h,            --help                    show this help message and exit.
    --btc_block                              Find latest Bitcoin blockchain info.
    --btc_date                               Find Bitcoin blockchain information from given date.
    --btc_address                            Find out balance and transaction information of given bitcoin address.
    --ssl_cipher                             List out all the ciphers used by given server.
    --ssl_bleed                              Check whether server is vulnerable to heart bleed flaw or not.
    --domain                                 Get bunch of detail of given website or organization.
    --email                                  Gather information of a given email address.
    --device                                 Find out devices which are connected to internet.
    --ip                                     Enumerate information from given IP Addresss.
    --skype_db                               Give the location of skype database in order to fetch all the information from that including chats and contacts.
    --malware                                Find out whether a given file is infected by malware or not.
    --carrier                                Give path of carrier file behind which you want to add text.
    --setgo_text                             Enter text to hide behind carrier file.
    --stego_find                             Give a stego file and it will try to find hidden text.
    
    """


printOnStart()
