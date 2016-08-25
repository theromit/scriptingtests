import csv
with open('/Users/romit/Downloads/spammer.csv') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        emailuser = row[0]
        fname = row[1]
        lname = row[2]
        emailname = emailuser[0:emailuser.find('@')]
        if emailuser.lower().find(fname.lower()) > 0:
            print fname + ' ' + emailuser + ' -First name included'
        elif emailuser.lower().find(lname.lower()) > 0:
            print lname + ' ' + emailuser + ' -Last name included'
        else: 
            print fname + ' ' + lname + ' ' + emailuser + ' -Spammer'