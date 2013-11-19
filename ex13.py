#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def writeImage(data):
    
    try:
        fout = open('woman2.jpg','wb')
        fout.write(data)
    
    except IOError, e:    
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
        
    finally:
        
        if fout:
            fout.close()       
    

try:
    con = lite.connect('test.db')
    
    cur = con.cursor()    
    cur.execute("SELECT Data FROM Images LIMIT 1")
    data = cur.fetchone()[0]
    
    writeImage(data)

    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()      
