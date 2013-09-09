'''
Run this script first!  Make sure you change the location of the files for reading and writing.
'''

import csv
from unidecode import unidecode

def interact():
	import code
	code.InteractiveConsole(locals=globals()).interact()

f = open('/path/to/yourfile.csv','rU')
#f = open('/Users/astorer/Work/aganderson/1952Letters-clean.csv','rU')

dr = csv.DictReader(f,fieldnames=["id","name","family","role","rankname","rank","samples"])

#g = open('/Users/astorer/Work/aganderson/AllLetters_proc.csv','w')
g = open('/path/to/AllLetters_proc.csv','w')
dw = csv.DictWriter(g,fieldnames=["id","sendername","rankname","rank","samples"])
dw.writeheader()

# question: what about two *'s in a letter?
allrecords = []
writer = ''
familynames = dict()
for row in dr:
    #print row
    d = dict()
    if row["id"] is "":
        d["id"] = lastid
    else:
        for r in allrecords:
            r["sendername"] = writer
            if r["rankname"] in familynames:
                r["rankname"] = r["rankname"] + ' ' + familynames[r["rankname"]]
            dw.writerow(r)
        allrecords = []
        familynames = dict()
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
        if row["family"] is not "":
            namedec = unidecode(unicode(row["name"],encoding='utf-8'))
            familynames[namedec] = unidecode(unicode(row["family"],encoding='utf-8'))
        d["samples"] = row["samples"]
        allrecords.append(d)
    except:
        1
