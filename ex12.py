#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def readImage():

    try:
        fin = open("woman.jpg", "rb")
        img = fin.read()
        return img
        
    except IOError, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        
        if fin:
            fin.close()


try:
    con = lite.connect('test.db')
    
    cur = con.cursor()
    data = readImage()
    binary = lite.Binary(data)
    cur.execute("INSERT INTO Images(Data) VALUES (?)", (binary,) )

    con.commit()    
    
except lite.Error, e:
    
    if con:
        con.rollback()
        
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()  
