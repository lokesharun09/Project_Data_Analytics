#Importing libraries to do this analysis
import pandas as pd
import pandas_datareader as pdr
import numpy as np

# #Setting the date range based on the datas in the traders_data.csv and creating keys to perform
start_date = '2020-01-01'
end_date = '2020-08-02'
stock1 = 'AMZN'
stock2 = 'FB'
stock3 = 'TSLA'

# #importing datas from the yahoo by using pandas_datareader
data_amazon = pdr.get_data_yahoo(stock1, start_date,
                          end_date)
data_amazon.to_csv('amazon.csv')

data_facebook = pdr.get_data_yahoo(stock2, start_date,  
                          end_date)
data_facebook.to_csv('facebook.csv')

data_tesla = pdr.get_data_yahoo(stock3, start_date,  
                          end_date)
data_tesla.to_csv('tesla.csv')

# #importing given test data
work = pd.read_csv('traders_data.csv')
work
work.info()

# #Rearranging the columns
work.columns
work['fullname'] = work['firstName'] + ' ' + work['lastName']
work = work.drop(columns = ['firstName', 'lastName'])
work = work[
    ['countryCode',
     'fullname',  
     'traderId', 
     'stockSymbol',
     'stockName', 
     'tradeId', 
     'price', 
     'volume',
     'tradeDatetime'
    ]
]
work
work.dtypes

#sort the datas based on timeframe
work = work.sort_values('tradeDatetime')
work.reset_index(drop=True, inplace=True)

# #Data Cleaning: Filling Nan values by logic
work = work.apply (lambda x: x.fillna(x.mean())
                  if x.dtype == 'float'
                  else x.fillna(x.value_counts().index[0]))
work.isnull().sum()
work['tradeDatetime'] = pd.to_datetime(work.tradeDatetime)
work.dtypes

amazon = pd.read_csv('amazon.csv')
amazon.info()
amazon.isna().sum()
amazon['Date'] = pd.to_datetime(amazon.Date)
amazon.info()
amazon.describe()

# #comparison of data by using the mean value of price,average value of price and the mean volume
result = work.loc[(work['price'] <3344) & (work['price'] >2336)
                    & (work['volume'] > 148)]
result

# #Grouped the data to findout the suspicious datas
# 1.by using fullname
result_groupby_fullname = result.groupby('fullname')
result_groupby_fullname.count()

# #Grouped the data to findout the suspicious datas
# 2.by using country code
result_groupby_countrycode = result.groupby('countryCode')
result_groupby_countrycode.count()

# Suspicous trader from the data:

#     Name             country
#     Brandon Berry	    NZ
#     Holly Simmons	    GT
#     Jordan Walker	    RU
# 
