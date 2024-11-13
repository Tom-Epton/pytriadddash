#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:31:54 2024

@author: tomepton
"""

import statsmodels as sm 
from statsmodels.tsa.ar_model import AutoReg
import numpy as np 
import pandas as pd 
from data_analysis import data 


se_data = data[data['experience_level'] == 'SE']

se_2020 = se_data[se_data['work_year'] == 2020]
se_2021 = se_data[se_data['work_year'] == 2021]
se_2022 = se_data[se_data['work_year'] == 2022]
se_2023 = se_data[se_data['work_year'] == 2023]
se_2024 = se_data[se_data['work_year'] == 2024]

def median_calculator(year):
    """
    year = dataframe 
    
    returns mean salary and standard deviation 
    
    
    """
    
    median_salary = np.mean(year['salary_in_usd'])
    std_dev_salary = np.std(year['salary_in_usd'])
    
    return median_salary, std_dev_salary

###################################### AXIS ARRAYS ###########################

y_axis = [median_calculator(se_2020)[0], median_calculator(se_2021)[0], 
          median_calculator(se_2022)[0], median_calculator(se_2023)[0],
          median_calculator(se_2024)[0]]

x_axis = np.arange(2020, 2025)

##############################################################################

def predict_next_values(y_axis, num_predictions=2):
    # Fit the autoregressive model to the data
    model = AutoReg(y_axis, lags=1).fit()
    
    # Forecast the next `num_predictions` values
    predictions = model.predict(start=len(y_axis), end=len(y_axis) + num_predictions - 1)
    
    # Return the predictions as a list
    return predictions.tolist()

predictions = predict_next_values(y_axis, 3)
x_pred = np.arange(2024, 2028)





