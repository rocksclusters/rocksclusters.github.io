#!/usr/bin/python

import os
import os.path
from bs4 import BeautifulSoup
import re
import csv, codecs, cStringIO

# next 3 classes are from https://docs.python.org/2.7/library/csv.html#csv-examples
class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
#-------------

# class for entry record.
class  Record:
    def __init__(self, id, writer):
        self.writer = writer
        self.id = id
        self.name = ""
        self.numCPU = 0
        self.typeCPU = ""
        self.clockCPU = 0 
        self.version = ""
        self.org = ""
        self.loc = ""
        self.monitored = ""
        self.notes = ""
        self.timestamp = ""

        self.flops = ""

    def addFields(self, 
                  time, name, numCPU, typeCPU, clockCPU, 
                  version, org, loc, mon, notes ):
        self.timestamp = time
        self.name = name
        self.numCPU = numCPU
        self.typeCPU = typeCPU
        self.clockCPU = clockCPU 
        self.version = "%s" % version
        self.org = org
        self.loc = loc
        self.monitored = mon
        self.notes = notes

    def addFlops(self, flops):
        self.flops = flops

    def show(self):
        self.writer.writerow([
            self.timestamp,
            self.name,
            self.numCPU, self.typeCPU, self.clockCPU,
            self.version, 
            self.org, 
            self.loc,
            self.monitored, 
            self.notes,
            self.flops
        ])

# strip html tags, etc, leave only plain text
def StripHtml (html):
    soup = BeautifulSoup(html)
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text


####### MAIN 

# partial name for the downloaded registartion record html file. 
partname = "details.php?id="

# open csv file
csvfile = open('NEWrecords.csv', 'wb')
writer = UnicodeWriter(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

# write csv file header
header = ["Timestamp", "Cluster Name", "Number of CPUs", "CPU Type", "CPU Clock"]
header = header + ["Rocks Version", "Organization", "Location", "Member of Rocks Grid" ]
header = header + ["Notes", "FLOPs"]
writer.writerow(header)

for index in range(2205) :
    #DEBUG  print "File", index+1
    fname =  "%s%d" % (partname , index+1)
    if not os.path.isfile(fname):
        continue
    f = open(fname)
    html = f.read()
    f.close()

    # rm control-M, join lines
    parts = html.split('\r\n')
    stri = ""
    for i in parts:
       stri = stri + '' + i[:-1]

    # remove multi-space 
    html = re.sub(' +',' ',stri) 

    # convert html to  plain text, strip all tags
    text = StripHtml(html)

    # collect fileds after "Vital Statistics"
    text1, text2 = text.split("Vital Statistics\n")
    parts = text2.split("\n")
    last = len(parts)
    if last != 28:
        print "ERROR in file  %s: has %d lines" % (index+1, last)
        print parts
        continue

    name = parts[1]
    numCPU = parts[3]
    typeCPU = parts[5]
    clockCPU = parts[7].split()[0]
    flops = parts[9].split()[0]
    version = parts[13]
    org = parts[15]
    loc = parts[17]
    mon = parts[21]
    notes = parts[25]
    time = parts[27]

    # fix rocks version
    if version in ["0.50", "2.60", "Rocks version", "N/A"]:
        version = "Other"

    # fix yes/no response
    if mon not in ["yes", "no"] :
        mon = "no"

    # create a record form the read info and write to csv file
    rec = Record(index+1, writer)
    rec.addFields(time, name, numCPU, typeCPU, clockCPU, version, org, loc, mon, notes )
    rec.addFlops(flops)
    rec.show()

# close csv file
csvfile.close()
