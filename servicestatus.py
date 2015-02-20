__author__ = 'jovin'
import urllib2,MySQLdb
import _mysql_exceptions
from mailer import Mailer
from mailer import Message

try:
    urllib2.urlopen('http://www.biller.in/biller')
except urllib2.HTTPError, e:
    message = Message(From="jovin@coolmindsinc.com",
                  To="jovin.25@gmail.com")
    message.Subject = "Biller seems to be down!"
    message.Html = """<p>Hi!<br>
        Biller service seems to be down.<br>
        Please look into the issue.</p>"""

    sender = Mailer('localhost')
    sender.send(message)
except urllib2.URLError, e:
    message = Message(From="jovin@coolmindsinc.com",
                  To="jovin.25@gmail.com")
    message.Subject = "Biller seems to be down!"
    message.Html = """<p>Hi!<br>
        Biller service seems to be down.<br>
        Please look into the issue.</p>"""

    sender = Mailer('localhost')
    sender.send(message)
try:
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="root", # your password
                      db="biller_test") # name of the data base
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    results = cursor.fetchone()
    ver = results[0]
except MySQLdb.Error, e:
    message = Message(From="jovin@coolmindsinc.com",
                  To="jovin.25@gmail.com")
    message.Subject = "Biller Mysql seems to be down!"
    message.Html = """<p>Hi!<br>
        Biller mysql service seems to be down.<br>
        Please look into the issue.</p>"""
