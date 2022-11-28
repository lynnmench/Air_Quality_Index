#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lynn Menchaca
Date: 23Nov2022

Project: Air Quality Index Prediction

"""

"""
Resources:
    - youtube -> Krish Naik -> Live Project Playlist

The purpose of this file is to

"""

from flask import Flask, render_template, url_for, request
import pandas as pd
import pickle

data_file_path = '/Users/lynnpowell/Documents/DS_Projects/Air_Quality_Index'

#load the model from disk
loaded_model = pickle.load(open(data_file_path + '/dtree_regression_model.pkl', 'rb'))
app  = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home_page.html')

@app.route('/predict',methods=['POST'])
def predict():
    df=pd.read_csv(data_file_path + '/Data_Files/csv_Data/full_clean_tokyo')
    my_predict = loaded_model.predict(df.iloc[:,:-1].values)
    my_predict = my_predict.tolist()
    return render_template('result_page.html',prediction=my_predict)

if __name__ == '__main__':
    app.run(debug = True)




