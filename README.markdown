MailDir Growl
=============

posts a [Growl](http://growl.info) notification whenever a new Mail is detected.
Lists sender and subject.

usage:

    maildirgrowl.py -m ~/Mail/gmail/INBOX/new [-a minutes]

-a is the age in minutes that causes an item to trigger a growl notify
    (used to prevent pileup of growl notifications while away from computer)

if you use offlineimap just add this to your cron or launchct


