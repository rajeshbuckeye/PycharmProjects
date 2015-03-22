__author__ = 'Rajesh'

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import datetime
import pandas.io.data

#sp500 = pd.io.data.get_data_yahoo('%5EGSPC',start=datetime.datetime(2000,01,01), end=datetime.datetime(2015,01,01))
#print sp500.head()
#sp500.to_csv('sp500_yahoo_csv')

c = pd.io.data.get_data_yahoo('C',start=datetime.datetime(2000,01,01), end=datetime.datetime(2015,01,01))

print(c)

#dataframe df
df = pd.read_csv('sp500_yahoo_csv')

df['H-L'] = df['High'] - df['Low']

df['Mov_Avg_H_L'] = pd.rolling_mean(df['H-L'],100)

df['Difference'] = df['Close'].diff()

print df['Mov_Avg_H_L'][200:250]

print df.head()

print df.columns.values

print df.describe()

df1 = df[['Open','Close']]

df1 = df1.rename(columns={'Open':'OPEN', 'Close':'CLOSE'})

df1['O-C'] = df1['OPEN'] - df1['CLOSE']

print df1.head()

#2D Plot
#df[['Close','High','Low','Open']].plot()
#plt.plot(df)

#3D Plot

#td = plt.figure().gca(projecttion='3d')
#td.scatter(df['High'], df['Low'])
#td.set_xlabel('Index')
#td.set_ylabel('High')
#td.set_zlabel('Low')

#plt.show()

#corelation
print df.corr()

#covariance
print df.cov()