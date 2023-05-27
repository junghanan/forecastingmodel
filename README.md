#Forecasting Model Project

When you are trying to predict future sales, you can use machine learning to predict it. However, Covid-19 has changed how customers spend. 
Thus, you need to build an agile forecasting model that can predict future based on a current trend. It will be very hard to predict using historical data since the trend is not applicable to 2020 or 2021 trend. 

If the trend is linear, you can apply y=a*x+b. However, the trend is showing an exponential trend. You cannot apply y=a*x+b. 
One way to do is to apply log function to change y=a*x+b into time function. 

Sometimes, you can obtain ideas from someone else's. I got an idea after observing Covid-19 Trend analysis. 

**3 major ideas to execute the analysis:** 
  1.Use log function to convert a linear model into an exponential model 
  2.Use Statsmodels to figure out coefficients of the exponential model
  3.Use coefficients to calculate forecasts 
  
**How to use log function?**

logX(t)=log(Xo)+log(b)t

log(Xo)=10.1951

Xo=e^10.1951 (getting the value of Xo)

Xo=26,771.682908406

log(b)=0.0466

b=e^0.00466 (getting the value of b)

b=1.0477028441 

Created an expontial function based on time: X(t)=26771.6929 x 1.0477^t

**What is Statsmodels?**

The detail can be found here: https://www.statsmodels.org/stable/index.html

Statsmodels is a Python module:
  1. Provides different classes and funcitons for estimation of many different statiscal models
  2. Conducts statiscal tests
  3. Allows statsical data exploration 
