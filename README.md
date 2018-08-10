# Bitcoin-Prediction

Bitcoin-Stock-price-prediction-with-Time-series-FBprophet-
Time Series Analysis in Python

Goal is to predict the range of Bitcoin stock price till 2022.

fbprophetis designed for analyzing time series with daily observations that display patterns on different time scales. It also has advanced capabilities for modeling the effects of holidays on a time-series and implementing custom changepoints, but we will stick to the basic functions to get a model up and running. fbprophet, can be installed with pip from the command line.

Steps:

Import the required packages
load the Bitcoin stock data from URL
visualize the data
check data types
Pre Processing
Converting necessary datat types
The prophet expects to be a ds column  that contains the datetime field and a y column that contains the value we are wanting to      forecast.

Build the model based on close value in the dataset and by checking apt changepoint the default value is 0.05. This hyperparameter is used to control how sensitive the trend is to changes, with a higher value being more sensitive and a lower value less sensitive

Make a future dataframe for 3 years

Make predictions and plot the forecast 
In the plot The black dots represent the actual values (notice how they stop at 2018), the blue line indicates the forecasted values, and the light blue shaded region is the uncertainty (always a critical part of any prediction). The region of uncertainty increases the further out in the future the prediction is made because initial uncertainty propagates and grows over time. This is observed in weather forecasts which get less accurate the further out in time they are made.

Visuallize the predicted model
Also Visualization in difftent time series to study trends
