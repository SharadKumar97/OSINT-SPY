from fullcontact import FullContact
from config import *
import json
fc=FullContact(fullcontact_api_key)


def fetchData(email_id):
    person = fc.person(email=email_id)
    data = person.json()
    try:
        print "Personal Information :: "
        print "Full Name :: "+ data['contactInfo']['fullName']
        print "Given Name :: "+ data['contactInfo']['givenName']
        print "Gender :: "+ str(data['demographics']['gender'])
        print "Website :: "+ str(data['contactInfo']['websites'])
        print "Full Address :: "+ str(data['demographics']['locationDeduced']['normalizedLocation'])
        print "City :: "+ str(data['demographics']['locationDeduced']['city']['name'])
        print "State :: "+ str(data['demographics']['locationDeduced']['state']['name'])
        print "Country :: "+ str(data['demographics']['locationDeduced']['country']['name'])
        print "\n"
    except:
        print "Unavailable"


    try:
        print "Employment Detail :: "
        for org in data['organizations']:
            print "Organization::"+org['name']+" "+"Start date::"+" "+org['startDate']+" "+"Job Title::"+" "+org['title']

    except:
        print " "
    print "\n"

    try:
        for soc in data['socialProfiles']:
            print "Social Profiles :: "+ " "+soc['url']
    except:
        print " "

    print "\n"
    print "Tags and Skills :: "
    try:
        for social in data['digitalFootprint']['topics']:
            print social['value']
    except:
        print " "
    print "\n"
    print "Photos and Pics :: "
    try:
        for pic in data['photos']:
            print "Url :: "+" "+ pic['url']

    except:
        print " "
