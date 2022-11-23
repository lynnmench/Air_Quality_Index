#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lynn Menchaca

Date: 18Nov2022

Project: Air Quality Index Prediction

"""

"""
Resources:
    - youtube -> Krish Naik -> Live Project Playlist


The purpose of this file is to pull the table from the web scrapped html file.
Then clean and combine the weather data and the air quality index data.

"""


from aqi_data_collection import aqi_avg_data
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

data_file_path = '/Users/lynnpowell/Documents/DS_Projects/Air_Quality_Index'

def met_data(month, year, city):
    
    #read the html file data as read byte form
    file_html = open(data_file_path+'/Data_Files/Html_Data/'+city+'_'+str(year)+'/'+city+'_'+str(month)+'.html',
                     'rb')
    plain_text = file_html.read()
    
    tempD = []
    finalD = []
    
    soup = BeautifulSoup(plain_text, 'lxml')
    
    #use inspect in the web page to see what the tabel class name is
    #pulling full tabel from this class
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):
        #each table
        for tbody in table:
            #each header
            for tr in tbody:
                #each row
                a = tr.get_text()
                tempD.append(a)
    
    #breaking out each feature (15) in a row
    rows = len(tempD) / 15
    
    #each number in the row data to fill in the columns
    for times in range(round(rows)):
        newtempD = []
        for i in range(15):
            newtempD.append(tempD[0])
            tempD.pop(0)
        finalD.append(newtempD)
            
    length = len(finalD)
    
    #removing extra row with full month average
    finalD.pop(length - 1)
    #removing headers
    finalD.pop(0)
    
    for a in range(len(finalD)):
        #droping features with null values seen on the website
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)
        
    return finalD


def data_combine(city, year, cs):
    for a in pd.read_csv(data_file_path+'/Data_Files/csv_Data/clean_'+city+'_'+str(year)+'.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


if __name__ == '__main__':
    if not os.path.exists(data_file_path+'/Data_Files/csv_Data'):
        os.makedirs(data_file_path+'/Data_Files/csv_Data')
    
    
    for city in ['tokyo','stl']:
        for year in range (2013, 2017):
            final_data = []
        
            with open(data_file_path+'/Data_Files/csv_Data/clean_'+city+'_'+str(year)+'.csv',
                      'w') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                wr.writerow(
                    ['T','TM','Tm','SLP','H','VV', 'V', 'VM','PM 2.5'])
                
            for month in range(1,13):
                temp = met_data(month, year, city)
                final_data = final_data + temp
                
            pm = getattr(sys.modules[__name__], 'aqi_avg_data')(year)
            
            if len(pm) == 364:
                pm.insert(364, '-')
                
            for i in range(len(final_data)-1):
                final_data[i].insert(8, pm[i])
                #final_data[i].insert(len(final_data[i])-1, pm[i])
                
            with open(data_file_path+'/Data_Files/csv_Data/clean_'+city+'_'+str(year)+'.csv',
                      'a') as csvfile:
                wr = csv.writer(csvfile, dialect='excel')
                
                for row in final_data:
                    flag = 0
                    
                    for elem in row:
                        if elem == '' or elem == '-':
                            flag = 1
                        
                    if flag != 1:
                        wr.writerow(row)


    for city in ['tokyo','stl']:
        data_2013 = data_combine(city, 2013, 600)
        data_2014 = data_combine(city, 2014, 600)
        data_2015 = data_combine(city, 2015, 600)
        data_2016 = data_combine(city, 2016, 600)
        
        total = data_2013 + data_2014 + data_2015 + data_2016
        
        with open(data_file_path+'/Data_Files/csv_Data/full_clean_'+city+'.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['T','TM','Tm','SLP','H','VV', 'V', 'VM','PM 2.5'])
            wr.writerows(total)


df_tokyo = pd.read_csv(data_file_path+'/Data_Files/csv_Data/full_clean_tokyo.csv')
df_stl = pd.read_csv(data_file_path+'/Data_Files/csv_Data/full_clean_stl.csv')



