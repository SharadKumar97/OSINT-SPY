# OSINT-SPY Search using OSINT (Open Source Intelligence)

Performs OSINT scan on email/domain/ip_address/organization using OSINT-SPY. It can be used by Data Miners, Infosec Researchers, Penetration Testers and cyber crime investigator in order to find deep information about their target.

# OSINT-SPY Documentation (beta)
	File Name     :     README
	Author        :     @sk_security
	Version       :     0.0.1
	Website       :     osint-spy.com

# Overview of this tool:
* Perform scan on IP Address / domain / email address / BTC(bitcoin) address / device
* Find out latest bitcoin block information
* List out all the ciphers supported by particular website and server
* Check whether a particular website is vulnerable to heartbleed or not ?
* Dump all the contacts and messages from skype database
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
```

# Required setup
* Python 2.7
* If you have pip installed then execute `pip install -r requirements.txt` else do the following.
* Execute `sudo python install_linux.py` (for installing all dependencies and libraries on linux)
* Use `python install_windows.py` (for installing all dependencies and libraries on windows)

# Contributors
	1. Sharad Kumar - @sk_security <twitter handler>

# Full Fledged tool documentation
> [http://osint-spy.com/command_line](http://osint-spy.com/command_line)
