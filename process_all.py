'''
Run this script first!  Make sure you change the location of the files for reading and writing.
'''

import csv
from unidecode import unidecode

f = open('/path/to/yourfile.csv','rU')
dr = csv.DictReader(f,fieldnames=["id","name","family","role","rankname","rank","samples"])

g = open('/path/to/AllLetters_proc.csv','w')
dw = csv.DictWriter(g,fieldnames=["id","sendername","family","rankname","rank","samples"])
dw.writeheader()

# question: what about two *'s in a letter?
allrecords = []
writer = ''
for row in dr:
    #print row
    d = dict()
    if row["id"] is "":
        d["id"] = lastid
    else:
        for r in allrecords:
            r["sendername"] = writer
            dw.writerow(r)
        allrecords = []
        writer = ''
        #print "reset writer to", writer
        d["id"] = row["id"]
        lastid = row["id"]        
    if '*' in row["role"]:
        if writer is not '':                
            print lastid, "needs inspection"
            #print writer, "is the last starred person"
        writer = unidecode(unicode(row["name"],encoding='utf-8')).split()[0] + unidecode(unicode(row["family"],encoding='utf-8'))
        #print "Writer: ", writer, "from row", row
    d["rank"] = row["rank"]
    try:
        d["rankname"] = unidecode(unicode(row["rankname"],encoding='utf-8')).split()[0].replace('?','')
        d["samples"] = row["samples"]
        d["family"] = row["family"]
        allrecords.append(d)
    except:
        1
