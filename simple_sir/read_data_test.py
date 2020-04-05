import pandas as pd 
import matplotlib.pyplot as plt
from datetime import datetime

def extract_country_data(df, country):
    date_format = '%m/%d/%y'
    datetime0 = datetime.strptime(df.columns[4], date_format)
    time = [(datetime.strptime(date, date_format) - datetime0).days for date in df.columns[4:]] 
    df_country = df.loc[df['Country/Region'] == country]
    values = [value for value in df_country.iloc[0][4:]]
    return time, values

country = 'Sweden'
df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
time_confirmed, confirmed = extract_country_data(df_confirmed, country)

df_deceased = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
time_deceased, deceased =  extract_country_data(df_deceased, country)

plt.plot(time_confirmed, confirmed, time_deceased, deceased)
plt.legend(('Confirmed','Deceased'))
plt.xlabel('Days')
plt.ylabel('Count')
plt.title(country)
plt.show()
