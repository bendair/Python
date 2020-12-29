import csv
import pandas as pd 
import numpy as np
#import geoviews as gv
#import geoviews.tile_sources as gvts
#from geoviews import dim, opts
#gv.extension('bokeh')

input_file = csv.DictReader(open("cal_cities.csv"))

#Variable initialisation
totalpop = 0
averagepop = 0
minpop = 10000000
mincity = ""
maxpop = 0
maxcity = ""
nol = 0 
o100k = 0
o250k = 0
o500k = 0
o1M = 0
citypop = 0

#Thousands seperator
# https://queirozf.com/entries/python-number-formatting-examples#use-commas-as-thousands-separator
    
for row in input_file:
    #print(row)
    #print(row['City'], row['Population_total'])
    #print(row['City'], "{:,}".format(int(row['Population_total'])))
  
    nol += 1
    citypop = int(row['Population_total'])
    
    if citypop > maxpop:
        maxpop = citypop
        maxcity = row['City']
        
    if citypop < minpop:
        minpop = citypop
        mincity = row['City']
    
    #totalpop += int(row['Population_total'])
    totalpop += citypop
    
    if int(row['Population_total'])>100000:
        o100k += 1
        if int(row['Population_total'])>250000:
            o250k += 1
            if int(row['Population_total'])>500000:
                o500k += 1
                if int(row['Population_total'])>1000000:
                    o1M += 1
                    print(row['City'], "{:,}".format(citypop), ">1M City ****SUPER CITY****")
                else:
                    print(row['City'], "{:,}".format(citypop), ">500k City")
            else:
                print(row['City'], "{:,}".format(citypop), ">250k City")
        else:
            print(row['City'], "{:,}".format(citypop), ">100k City")
    else:
        print(row['City'], "{:,}".format(citypop))
    
#print('Total Population of all cities:',totalpop )
print()
print("Total Population of all cities: {:,}".format(totalpop))
print("Average Population of all cities: {:,.2f}".format(totalpop/nol)) 
print("Smalled city by popupation is", mincity,"with a minimum of: {:,}".format(minpop), "people")
print("Largest city by popupation is", maxcity,"with a maximum of: {:,}".format(maxpop), "people")
print("Number of cities:", nol)
print("Number of cities over 100,000 people is", o100k)
print("Number of cities over 250,000 people is", o250k)
print("Number of cities over 500,000 people is", o500k)
print("Number of cities over 1,000,000 people is", o1M)