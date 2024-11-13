#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:16:49 2024

@author: tomepton


so far this has taken 120 minutes 
"""

# streamlit_wind_tunnel.py
import streamlit as st
import pandas as pd
import plotly.express as px
from data_analysis import data 
from salary_projections import x_axis, y_axis, predictions, x_pred 
import plotly.graph_objects as go
import numpy as np
from scipy.interpolate import make_interp_spline




st.set_page_config(
    page_title="Pytri Data Services",
    page_icon="logo.ico",  # Replace with the path to your logo file
    layout="wide"
)

# Sidebar for logo and contact information
st.sidebar.image("logo.png", use_column_width=True)  # Replace 'logo.png' with your image filename
st.sidebar.markdown("### Pytri Data Services")
st.sidebar.write("_Turning Data into Information_")

st.sidebar.write(
    
    
    """
    **Data Analytics Dashboard**  
    This dashboard was created by Pytri Data Services to help you explore this dataset - as well 
    as serving as a demonstration of what a couple of hours of our time will buy you.
    
    For enquiries:
    [📧 Contact Us](mailto:hello@pytridata.com)
    """
)

st.title("How much do you have to pay data scientists?")
st.markdown("""
---
**Salary distribution and projections**

This dashboard visualises salary data from a range of data scientists surveryed between 2020 and 2024.
The second plot shows the salaries of senior engineers and a projection of where these salaries will go.
Use this tool to identify trends, peak ranges, and the overall distribution of salaries. The plots are fully 
interactive, you can zoom in on specific salary bands for example. 

Your company could gain insights from data products such as this, drop us an email [here](mailto:hello@pytridata.com).

This dashboard took 2 hours to create - for more information on our pricing, [click here](https://brainy-aquarius-6ed.notion.site/Website-and-Application-Management-Pricing-7bbeee6ccaa34517b152eeb73a4b2ff9).
""")

# Introductory Markdown
st.markdown("""
<hr style="border:0.5px solid gray">
<p style="font-size:14px; color: gray;">
Below is a preview of the dataset, showcasing the first five rows. Each row represents a record with multiple columns, providing insights into different attributes captured in this data. This particular data was from a global 
survey of datascientists with various conditions imposed for inclusion. You can find out more on Kaggle regarding the data used if you wish.
</p>
<hr style="border:0.5px solid gray">
""", unsafe_allow_html=True)


# Display the first five rows of the dataframe
st.write(data.head())

# Closing Markdown for additional notes or data context
st.markdown("""
<hr style="border:0.5px solid gray">
<p style="font-size:14px; color: gray;">
This initial preview offers a glimpse into the dataset’s structure, allowing you to understand column names and data types. For more detailed exploration, you can use other interactive features in this dashboard. We've included two plots for demonstration purposes. On a typicl client dashboard will be 10-100 times the size of this.
</p>
<hr style="border:0.5px solid gray">
""", unsafe_allow_html=True)


fig = px.histogram(
        data, 
        x='salary_in_usd', 
        nbins=(max(data['salary_in_usd']) // 5000),  # Buckets of 5000
        title='Salary Distribution in USD',
        labels={'salary_in_usd': 'Salary (USD)'},
    )
    

fig.update_layout(
        xaxis_title="Headline salary in USD - all levels",
        yaxis_title="Frequency",
        xaxis=dict(dtick=100000),  # Tick every 50k for clarity
        bargap=0.1
    )

# display
st.plotly_chart(fig)

############ PROJECTIONS 

# Plotly figure setup
fig2 = go.Figure()

# Add actual y_axis data
fig2.add_trace(go.Scatter(
    x=x_axis,
    y=y_axis,
    mode='lines',
    name='Actual Salary',
    line=dict(color='royalblue', width=3)
))

# Add predictions data as points with circles around them to represent errors
fig2.add_trace(go.Scatter(
    x=x_pred,
    y=predictions,
    mode='markers',  # Change to 'markers' to display points
    name='Predicted Salary',
    marker=dict(
        color='firebrick',  # Color of the marker fill
        size=12,             # Size of the circle
        line=dict(
            color='black',  # Outline color of the circle
            width=2         # Outline width
        ),
        symbol='circle'     # Ensures markers are circular
    )
))




fig2.update_layout(
    title="Forecasted Mean Salary Progression for Data Scientists",
    xaxis_title="Time",
    yaxis_title="Salary in USD",
    legend=dict(
        x=0.01, y=0.99,
        bordercolor="Black",
        borderwidth=1
    )
)

# Streamlit dashboard display
#st.title("")
st.markdown("""
<hr style="border:0.5px solid gray">
<p style="font-size:14px; color: gray;">
The following plot is the salaries of the senior engineers pulled from the broader 
data set visualised above. We've plotted the mean salary for each year in the dataset 
and used an augmented autoregression model to forecast the next 3 years. We also used the same model to predict 2024's salary from the data of 2020 to 2023 so you 
can get an idea of how close the forecasted value got to the real salary data from 2024. To 
predict 2025 and 2026 the real 2024 value was used.'
</p>
<hr style="border:0.5px solid gray">
""", unsafe_allow_html=True)

st.plotly_chart(fig2)



"""
Your company could gain insights from data products such as this, drop us an email: hello@pytridata.com.

"""









