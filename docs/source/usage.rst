Usage
=====

OSINT-SPY is very handy tool and easy to use.
All you have to do is just have to pass values to parameter.
In order to start OSINT-SPY just write
::

    python osint-spy.py


--btc_block
^^^^^^^^^^^

--btc_block parameter gives you the information
of the latest bitcoin block chain.
::

    python osint-spy.py --btc_block


--btc_date
^^^^^^^^^^
--btc_date parameter will give you an information
of bitcoin block chain from given date.
::

    python osint-spy.py --btc_date 20170620


--btc_address
^^^^^^^^^^^^^
--btc_address will give you an information
about particular bitcoin owner.
::

    python osint-spy.py --btc_address 1DST3gm6JthxhuoNKFqXrdpzPFfz1WgHpW


--ssl_cipher
^^^^^^^^^^^^
-ssl_cipher will show you all the ciphers
supported by given website.
::

    python osint-spy.py --ssl_cipher google.com


--ssl_bleed
^^^^^^^^^^^
--ssl_bleed will find out whether given website
is vulnerable to heartbleed or not ?
::

    python osint-spy.py --ssl_bleed google.com


--domain
^^^^^^^^
--domain will give you in depth-information about
particular domain including whois, dns, ciphers,
location and so more.
::

    python osint-spy.py --domain google.com


--email
^^^^^^^
--email will gather information about given
email address from various public sources.
::

    python osint-spy.py --email david@google.com


--device
^^^^^^^^
--device will search for a given device from
shodan and will list out all the available
devices on public IP.
::

    python osint-spy.py --device webcam


--ip
^^^^
--ip will gather all the information of given
IP Address from public sources.
::

    python osint-spy.py --ip 45.76.151.11


--malware
^^^^^^^^^
--malware will send a given piece of file to
virustotal and will give you a result whether given file
is malware or not?
::

    python osint-spy.py --malware abc.exe


