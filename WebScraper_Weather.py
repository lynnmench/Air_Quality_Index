#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lynn Menchaca

Date: 18Nov2022

Project: Air Quality Index Prediction

"""

"""
Resources:
    - World Weather -> (https://en.tutiempo.net/)
    - youtube -> Krish Naik -> Live Project Playlist

The purpose of this file is to web scrape the weather data
for different cities and years.

"""


import os
import time
import requests
import sys

data_file_path = '/Users/lynnpowell/Documents/DS_Projects/Air_Quality_Index'

#Webscraping to collection weather temperature for each day

def pull_weather_html(start_year, end_year):
    for year in range(start_year,end_year+1):
        for month in range(1,13):
            
            #Tokyo Japan weather - website
            if (month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-476620.html'.format(month,year)
                
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-476620.html'.format(month,year)
                
            #scrape all the information in to a utf-8 formated file
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            #print(text_utf)
            
            #Checking if folder exists if not creating it
            if not os.path.exists(data_file_path+'/Data_Files/Html_Data/tokyo_{}'.format(year)):
                os.makedirs(data_file_path+'/Data_Files/Html_Data/tokyo_{}'.format(year))
            #saving web scraped information in to the folder
            with open(data_file_path+'/Data_Files/Html_Data/tokyo_{}/tokyo_{}.html'.format(year,month),'wb') as output:
                output.write(text_utf)
                
                
            #Saint Louis MO (Spirit Of St. Louis Airport)
            if (month < 10):
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-724345.html'.format(month,year)
                
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-724345.html'.format(month,year)
                
            #scrape all the information in to a utf-8 formated file
            texts=requests.get(url)
            text_utf=texts.text.encode('utf=8')
            
            #Checking if folder exists if not creating it
            if not os.path.exists(data_file_path+'/Data_Files/Html_Data/stl_{}'.format(year)):
                os.makedirs(data_file_path+'/Data_Files/Html_Data/stl_{}'.format(year))
            #saving web scraped information in to the folder
            with open(data_file_path+'/Data_Files/Html_Data/stl_{}/stl_{}.html'.format(year,month),'wb') as output:
                output.write(text_utf)
            
            #San Antonio Texas - International Airport
            #https://en.tutiempo.net/climate/01-2013/ws-722530.html
            
        sys.stdout.flush()
        
        


if __name__ == '__main__':
    start_time = time.time()
    pull_weather_html(2013, 2021)
    stop_time = time.time()
    print('Time taken: ', (stop_time-start_time))
    
    

