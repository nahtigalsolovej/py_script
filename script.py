
import pydap.client
from pydap.client import open_url
import datetime
import random
import sqlite3 as lite

url='http://opendap.solab.rshu.ru:8080/opendap/allData/SSMI/f13/bmaps_v07/y1995/m05/f13_19950503v7.gz'
dataset = open_url(url)

wspd = dataset.wspd[:,:,:]
time = dataset.time[:,:,:]

wspd_scale_factor = dataset.wspd.scale_factor
wspd_add_offset = dataset.wspd.add_offset
time_scale_factor = dataset.time.scale_factor
time_add_offset = dataset.time.add_offset

d=dataset.attributes['SSMI_GLOBAL']['original_filename']
mydate = d[d.index('_')+1:d.index('_')+9]
year=mydate[0:4]
mon=mydate[4:6]
day=mydate[6:8]
#print year, mon, day
filedate = datetime.date(int(year), int(mon), int(day))
#print filedate

con = lite.connect('test.db')
cur = con.cursor()
cur.execute("DELETE from datatest")

for i in range(wspd.shape[0]):
    for j in range(wspd.shape[1]):

        value = wspd[i, j, 0]
        if value < 250:
            value = value * wspd_scale_factor + wspd_add_offset

        t = time[i, j, 0]
        if t < 250:
            t = t * time_scale_factor + time_add_offset
            hour = int(t/60)
            min = t%60
            filetime = datetime.time(int(hour), int(min))

        else:
            filetime = datetime.time(0, 0)

        date = str(filedate) + ' ' + str(filetime)

        lat = random.randrange(70, 75, 1)
        lon = random.randrange(20, 25, 1)

        test = (date, float(value), lat, lon)

        if value < 250:
            cur.execute("INSERT INTO datatest(datetime, wind, lat, lon) VALUES(?, ?, ?, ?)", test)

con.commit()
con.close()