#! /usr/bin/env python

import os, sys , requests, smtplib
from lxml import html

print "Cruises :)"

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( EMAIL, EMAIL_PASSWORD)
try:
    response = requests.get('https://www.ncl.com/cruises/11-day-panama-canal-round-trip-from-miami-PEARL11MIACTGPCGCLNLIORTBBZECMAMIA/Dates/December-2015?destinations=4294934550&numberOfGuests=4294915774&cruiseHotel=1&cruiseTour=1&state=null&pageSize=10&sailmonths=4294925773&cruise=1&sortBy=Featured&cruiseHotelAir=1&currentPage=1&&itineraryCode=PEARL11MIACTGPCGCLNLIORTBBZECMAMIA')

    print response

    tree = html.fromstring(response.text)
    stuff = tree.xpath('//*[@id="teaLeaf-span-voyage7921939-INSIDE-2-250"]/text()')

    price = int(stuff[0].replace('$', ''))
    if price < 999:
        print 'send sms'
    
        test = "\nCurrent price of the cruise: $%d" % price
        server.sendmail(EMAIL, 'phone_number@txt.att.net', test)
        server.sendmail(EMAIL, 'phone_number@txt.att.net', test)


    else:
        print "Prices is still high"
except Exception, e:
    print e
    server.sendmail(EMAIL, 'phone_number@txt.att.net', "There was an error in the %s script" % __file__)

server.quit()

