[![Cactuscon](http://static1.squarespace.com/static/56b38e2aa3360ce530d55c24/t/56b3fc1bf850820fe762454d/1506815794423/?format=1500w)](http://cactuscon.com/) US



# OSINT-SPY Search using OSINT(Open Source Intelligence)
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
* Use install_linux.py      (for installing all dependencies and libraries on linux)
* Use install_windows.py    (for installing all dependencies and libraries on windows)




# Contributors
	1. Sharad Kumar - @sk_security <twitter handler>




# Documentation
# Setting up the enviornment
```
Installing and using OSINT-SPY is very easy.Installation process is very simple and is of 4 steps.
1.Downloading or cloning OSINT-SPY github repository.
2.Downloading and installing all dependencies.
3.Generating API Keys
4.Adding API Keys in config file

Let's Begin !!

Step 1 - Download OSINT-PSY on your system.

In order to install OSINT-SPY simply clone the github repository.Below is the command which you can use in order to clone OSINT-SPY repository.
git clone https://github.com/SharadKumar97/OSINT-SPY.git
Step 2 - Downloading and Installing dependencies.

Once you clone OSINT-SPY, you will find one directory name as OSINT-SPY. Just go that directory and install dependencies. If you are using OSINT-SPY on windows then run install_linux.py file and if you are using linux then run install_linux.py
python install_linux.py

OR
python install_windows.py

```
# Generating API Keys

```
We need some API Keys before using this tool.Following are the API's which we are using in this tool for a time being.
1.Clearbit API
2.Shodan API
3.Fullcontact API
4.Virus_Total API
5.EmailHunter API

Clearbit API

    Register yourself at Clearbitand activate your account.
    Once you login, you will find one section of API. Go there and copy your secret API Key and paste inside config.py file.
    Config.py file can be find in modules directory of OSINT-SPY.



Shodan API

    Register yourself at Shodan and activate your account.
    Once you activated your account then login to Shodan.
    Once you login, you will find an API key in overview tab.
    Copy that key and paste inside config.py file.



FullContact API

    Register yourself at Full Contact. You can sign up by using your email or you can Sign Up with Google.
    Once you login, you will find your API Key on front of your dashboard.
    Just copy that key and paste it inside config.py file.



VirusTotal API

    Register yourself at VirusTotal .
    Once you login, you will find My Api Key section in your profile menu. Just go there and copy your public API Key and paste in config.py file.



EmailHunter API

    Register yourself at Email Hunter .
    Once you login, go to API tab and click on EYE icon to view your API Key.
    Copy your API Key in config.py file.


```
# Usage 

```
OSINT-SPY is very handy tool and easy to use.All you have to do is just have to pass values to parameter.In order to start OSINT-SPY just write -- 
python osint-spy.com

--btc_block

    --btc_block parameter gives you the information of latest bitcoin block chain.

Usage:
python osint-spy.py   --btc_block

--btc_date

    --btc_date parameter will give you an information of bitcoin block chain from given date.

Usage:
python osint-spy.py   --btc_date 20170620

--btc_address

    --btc_address will give you an information about particular bitcoin owner.

python osint-spy.py  --btc_address 1DST3gm6JthxhuoNKFqXrdpzPFfz1WgHpW

--ssl_cipher

    --ssl_cipher will show you all the ciphers supported by given website.

python osint-spy.py  --ssl_cipher google.com

--ssl_bleed

    --ssl_bleed will find out whether given website is vulnerable to heartbleed or not ? .

python osint-spy.py  --ssl_bleed google.com

--domain

    --domain will give you in depth-information about particular domain including whois,dns,ciphers,location and so more.

python osint-spy.py  --domain google.com

--email

    --email will gather information about given email address from various public sources.

python osint-spy.py  --email david@toorcon.org

--device

    --device will search for a given device from shodan and will list out all the available devices on public IP.

python osint-spy.py  --device webcam

--ip

    --ip will gather all the information of given IP Address from public sources.

python osint-spy.py  --ip 127.0.0.1

--skype_db

    --skype_db will find out all the contacts and message history from given skype database.This can be useful for forensics investigator.In Windows,Skype database can be found in AppData\Roaming\Skype\(Your username)\main.db and in Mac OSX , database can be found in /Users/(Your mac user anme)/Library/Support/Skype/(your skyoe username)/main.db

python osint-spy.py   --skype_db main.db

--malware

    --malware will send a given piece of file to virustotal and will give you a result whether given file is malware or not? .

python osint-spy.py  --malware abc.exe

--carrier and --stego_text

    --carrier and --stego_text are used to hide text behind any image.
    --carrier will specify the image behind which you want to hide the text.
    --stego_text will specify the text you want to add.

python osint-spy.py  --carrier image.jpg    --stego_text This_is_secre_text

--stego_find

    --stego_find will find out hidden text behind any image.

python osint-spy.py  --stego_find hidden.jpg

```

