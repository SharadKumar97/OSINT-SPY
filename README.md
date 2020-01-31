# OSINT-SPY Search using OSINT(Open Source Intelligence)
Performs OSINT scan on email/domain/ip_address/organization using OSINT-SPY. It can be used by Data Miners, Infosec Researchers, Penetration Testers and cyber crime investigator in order to find deep information about their target.

* Release 2.0
* Added Python 3 support.
* This is the initial release for Python 3, new features will be pushed next week. 

# OSINT-SPY Documentation (beta)
	File Name     :     README
	Author        :     @sk_security
	Version       :     2.0
	Website       :     https://docs.osint-spy.io



# Overview of this tool:
* Perform scan on IP Address / domain / email address / BTC(bitcoin) address / device
* Find out latest bitcoin block information
* List out all the ciphers supported by web servers.
* SSL heart bleed scan
* Analyze malware or malicous file remotely


# Licenses information
OSINT-SPY and its documents are covered with GPL-3.0 (General Public License v3.0)


## Using OSINT-SPY
```
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

```

# Contributors
	1. Sharad Kumar - @sk_security <twitter handler>

# Documentation

* For detailed documentation please go to https://docs.osint-spy.io
