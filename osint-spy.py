import argparse
from modules import (get_bitcoin_data, get_ciphers, heart_bleed,
                     get_company_detail, fetch_email, get_device, ip_details, VirusTotal)


parser = argparse.ArgumentParser()
parser.add_argument("--btc_block", help="Get latest bitcoin block info.", action="store_true")
parser.add_argument("--btc_date", help="Get bitcoin block info by date, example - 20190614", type=int)
parser.add_argument("--btc_address", help="Get info of any bitcoin wallet address")
parser.add_argument("--ssl_cipher", help="List out supported SSL ciphers used by any domain")
parser.add_argument("--ssl_bleed", help="Check whether server is vulnerable to heart bleed or not")
parser.add_argument("--domain", help="Do domain recon")
parser.add_argument("--email", help="Do email recon")
parser.add_argument("--device", help="Explore the Internet of Things. Example - opensips,asterisk,juniper,windows10")
parser.add_argument("--ip", help="WHOIS IP Lookup")
parser.add_argument("--malware", help="Send files to VirusTotal for malware analysis")
parser.add_argument("--json", help="Show output in JSON format", action="store_true")
args = parser.parse_args()

if args.btc_block:
    url = 'https://chain.api.btc.com/v3/block/latest'
    get_bitcoin_data(url, args.json)
    exit()

elif args.btc_date:
    date = args.btc_date
    url = f'https://chain.api.btc.com/v3/block/date/{date}'
    get_bitcoin_data(url, args.json)
    exit()

elif args.btc_address:
    address = args.btc_address
    url = f'https://chain.api.btc.com/v3/address/{address}'
    get_bitcoin_data(url, args.json)
    exit()

elif args.ssl_cipher:
    server = args.ssl_cipher
    get_ciphers(server)
    exit()

elif args.ssl_bleed:
    server = args.ssl_bleed
    heart_bleed(server)
    exit()

elif args.domain:
    domain = args.domain
    get_company_detail(domain, args.json)
    exit()

elif args.email:
    email_id = args.email
    fetch_email(email_id, args.json)
    exit()

elif args.device:
    device_name = args.device
    get_device(device_name, args.json)
    exit()

elif args.ip:
    ip = args.ip
    ip_details(ip, args.json)
    exit()

elif args.malware:
    mal_path = args.malware
    api = VirusTotal()
    api.send_malware(mal_path, args.json)
    exit()

else:
    print("""

       @@@@@@@@@     @@@@@@@@@  |  @@      @  88888|88888       @@@@@@@@@  8@@@@@@@@  8           @
      88888888888    |          |  @ @     @       |            |          8       @    8        @
      @@@@@@@@@@@    |          |  @  @    @       |            |          8       @      8     @
      88888888888    |@@@@@@@@  |  @   @   @       |      ----  |@@@@@@@@  8@@@@@@@@        8  @
      @@@@@@@@@@@            |  |  @    @  @       |                    |  8                  @
      @@@@@@@@@@@            |  |  @     @ @       |                    |  8                 @
       888888888     @@@@@@@@|  |  @      @@       |            @@@@@@@@|  8                @

                                         Search using OSINT
                                      Website: https://docs.osint-spy.io

        Usage: osint-spy.py [options]
        Options:
        -h,            --help                    show this help message and exit
        --btc_block                              Get latest bitcoin block info
        --btc_date                               Get bitcoin block info by date, example - 20190614
        --btc_address                            Get info of any bitcoin wallet address
        --ssl_cipher                             List out supported SSL ciphers used by any domain
        --ssl_bleed                              Check whether server is vulnerable to heart bleed or not
        --domain                                 Do domain recon
        --email                                  Do email recon
        --device                                 Explore the Internet of Things. Example - opensips,asterisk,juniper,windows10
        --ip                                     WHOIS IP Lookup
        --malware                                Send files to VirusTotal for malware analysis
        --json                                   Show output in JSON format
        """)
