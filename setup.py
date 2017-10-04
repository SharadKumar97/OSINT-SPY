import os
import platform

if (platform.system() != "Windows"):
    os.system('sudo apt-get install python-pip')
    os.system('sudo pip install clearbit')
    os.system('sudo pip install shodan')
    os.system('sudo pip install fullcontact.py')
    os.system('sudo pip install steganography')
    os.system('sudo pip install requests')
    os.system('sudo pip install sslscan')
    os.system('sudo pip install pythonwhois')
else:
    os.system('C:\Python27\Scripts\pip install clearbit')
    os.system('C:\Python27\Scripts\pip install shodan')
    os.system('C:\Python27\Scripts\pip install fullcontact.py')
    os.system('C:\Python27\Scripts\pip install steganography')
    os.system('C:\Python27\Scripts\pip install requests')
    os.system('C:\Python27\Scripts\pip install sslscan') 
