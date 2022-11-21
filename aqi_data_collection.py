#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lynn Menchaca

Date: 16Nov2022

Project: Air Quality Index Prediction

"""

"""
Resources:
    - youtube -> Krish Naik -> Live Project Playlist
    - air quality index was pulled using OpenWeather API
    - air quality data was provided by Krish Naik

The purpose of this file is to clean and process the air quality data.

    - take an average of the feature 'PM2.5'
    - This will convert the air quality index from hourly to dayly.
This will be the independent feature when combined with the weather data collecte




"""




#air quality data
#have to convert the air quality data for each hour and take an average for the day
#clean the data
#weather collected data
#converting weather data from html file to cvs file
#combine data sets: independent feature is the air quality data

import pandas as pd
import matplotlib.pyplot as plt

data_file_path = '/Users/lynnpowell/Documents/DS_Projects/Air_Quality_Index'

def aqi_avg_data(year):
    temp_i = 0
    average = []
    
    # chunksize takes that many records at a time -> 24 for each hour in the day
    for rows in pd.read_csv(data_file_path+'/Data_Files/AQI_Data/aqi'+str(year)+'.csv',chunksize=24):
        add_var = 0
        avg = 0.0
        data = []
        df = pd.DataFrame(data=rows)
        
        #using PM2.5 as our air quality values
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
            
        # irrerating though each aqi and summing all numbers to later take an average
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            #handling numeric values as strings and skiping over bad data
            elif type(i) is str: 
                if i != 'NoData' and i!= 'PwrFail' and i != '---' and i != 'InVld':
                    temp=float(i)
                    add_var=add_var + temp
                    
        avg = add_var/24
        temp_i = temp_i + 1
        
        average.append(avg)
    return average


if __name__ == '__main__':
    
    for year in range(2013,2019):
        lst_year = aqi_avg_data(year)
        plt.plot(range(0,len(lst_year)),lst_year,label=str(year)+' data')
        plt.xlabel('Day')
        plt.ylabel('PM 2.5')
        plt.legend(loc='upper right')
        plt.show()



