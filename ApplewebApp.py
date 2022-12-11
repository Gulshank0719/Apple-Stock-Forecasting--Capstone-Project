# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:32:52 2022

@author: yogesh kand
"""

import pandas as pd
import streamlit as st
from pickle import load
import statsmodels.api as sm
import matplotlib.pyplot as plt
#import datetime
#from datetime import datetime


data_close = load(open('df.pkl','rb'))

# creating a function for Prediction

from PIL import Image
image = Image.open("bull-market.jpg")
st.image(image)

 # giving a title

# giving a title

html_temp="""
<div style ="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;"> Apple Stock Forecasting App

"""

st.markdown(html_temp,unsafe_allow_html=True) 

#date = st.date_input('Date',min_value=datetime.datetime(2020,1,1))

periods = st.number_input('Number of Days',min_value=1)

datetime = pd.date_range('2020-01-01', periods=periods,freq='B')
date_df = pd.DataFrame(datetime,columns=['Date'])

#datetime = pd.date_range(date, periods=periods,freq='B')
#date_df = pd.DataFrame(datetime,columns=['Date'])   



model_sarima_final = sm.tsa.SARIMAX(data_close.Close,order=(1,1,1),seasonal_order=(2,1,0,12))
sarima_fit_final = model_sarima_final.fit()
forecast = sarima_fit_final.predict(len(data_close),len(data_close)+periods-1)
forecast_df = pd.DataFrame(forecast)
forecast_df.columns = ['Close']

data_forecast = forecast_df.set_index(date_df.Date)
st.write(data_forecast)

#fig = plt.plot(data_forecast, label='Forecast',color='red')
#st.line_chart(data_forecast)

fig,ax = plt.subplots()
ax.plot(data_forecast)
ax.set_title('Apple Stock Forecast')
ax.set_xlabel('Date')
ax.set_ylabel('Stock Price')
ax.grid(True)
st.pyplot(fig)



