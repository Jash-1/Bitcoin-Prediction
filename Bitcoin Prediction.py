
# coding: utf-8

# In[1]:


#importing Libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import time
import seaborn as sns
import datetime
from fbprophet import Prophet 


# In[2]:


#importing the dataset
bh = pd.read_html("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end="+time.strftime("%Y%m%d"))[0]


# In[4]:


bh.head(5)


# In[5]:


#viewing data types
bh.dtypes


# In[6]:


#converting necessary datat types
bh['Date'] = pd.DatetimeIndex(bh['Date'])


# In[7]:


bh.dtypes


# In[8]:


# The prophet expects to be a ds column  that contains the datetime field
#and a y column that contains the value we are wanting to forecast.
bh = bh.rename(columns={'Date': 'ds', 'Close**': 'y'})


# In[9]:


bh.tail(5)


# In[10]:


#Visualizing given data
plt.plot(bh['ds'], bh['y'])
plt.title('Bitcoin Price')
plt.ylabel('Price');
plt.xlabel('Time');
plt.show()


# In[11]:


#Creating and fitting Model to data 
model = Prophet(interval_width=0.95)
model.fit(bh)


# In[12]:


#Creating future dates to predict(for 3 years or 36 months)
future_dates = model.make_future_dataframe(periods=36, freq='MS')
future_dates.tail()


# In[13]:


#Forcasting Future Dates
forecast = model.predict(future_dates)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()


# In[17]:


model.plot(forecast, xlabel = 'Date', ylabel = 'closing value', uncertainty=True)
plt.title('Bitcoin forecast')
plt.show();


# In[19]:


#Visualization in difftent time series
model.plot_components(forecast)

