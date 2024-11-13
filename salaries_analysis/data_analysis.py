#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:27:46 2024

@author: tomepton
"""

import pandas as pd

# Load the CSV file
file_path = 'salaries_DS.csv'  
data = pd.read_csv(file_path)

# display basic info
print("First 5 rows of the dataset:")
print(data.head())

print("\nSummary of the dataset:")
print(data.describe())


print("\nColumn names:")
print(data.columns)


