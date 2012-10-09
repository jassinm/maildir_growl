#!/usr/bin/env python
# encoding: utf-8

import email
import subprocess
import time
from optparse import OptionParser
#from dateutil.parser import parse as dateparser
import os

imagefile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
        '77.png')


def growl_message(message):

    msg_from = message['From']
    name, address = email.utils.parseaddr(msg_from)
    msg_subject = message['Subject']
    # msg_date = dateparser(message['Date'])
    msg_id = message['Message-id']

    message = '%s\n%s' % (name, msg_subject)
    subprocess.check_call(['/usr/local/bin/growlnotify',
                     '-n', 'OfflineIMAP',
                     '-m', message,
                     '--image', imagefile,
                     '-d', msg_id])

def is_too_old(file_path, max_minutes):

    if max_minutes == 0:
        return False
    file_time = os.stat(file_path).st_mtime
    current_time = time.time()
    if ((current_time - file_time) / 60) > max_minutes:
        return True
    return False


def main():

    usage = 'usage: %prog [options] user -h for help'
    parser = OptionParser(usage)
    parser.add_option('-m' , '--maildir', action='store',
            type='string', dest='maildir', help='path to dir to check mails')
    parser.add_option('-a' , '--maxminutes', action='store',
            type='float', dest='max_minutes', help='greater than this value prevents growl message')
    (options, args) = parser.parse_args()

    max_age = 0
    if options.max_minutes:
        max_age = options.max_minutes

    if options.maildir:
        for file_ in os.listdir(options.maildir):
            fullpath = os.path.join(options.maildir, file_)
            if is_too_old(fullpath, max_age):
                continue
            with open(fullpath) as mail_file:
                msg = email.message_from_file(mail_file)
                growl_message(msg)

if __name__ == '__main__':
    import sys
    status = main()
    sys.exit(status)
