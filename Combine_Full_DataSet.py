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


The purpose of this file is clean and combine the weather data and the
air quality index data.

"""


from aqi_data_collection import aqi_avg_data
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os

data_file_path = '/Users/lynnpowell/Documents/DS_Projects/Air_Quality_Index'

def met_data(month, year):
    
    #read the html file data as read byte form
    file_html = open(data_file_path+'/Data_Files/Html_Data/tokyo_{}/tokyo_{}.html'.format(year,month),
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
    
    #removing Day feature
    finalD.pop(length - 1)
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


if __name__ == '__main__':
    if not os.path.exists(data_file_path+'/Data_Files/csvData'):
        os.makedirs(data_file_path+'/Data_Files/csvData')
    
    for year in range (2013, 2021):
        final_data = []
        
        with open(data_file_path+'/Data_Files/csvData/')













