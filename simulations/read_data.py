import pandas as pd
from datetime import datetime

def extract_country_data(df, country):
    date_format = '%m/%d/%y'
    datetime0 = datetime.strptime(df.columns[4], date_format)
    time = [(datetime.strptime(date, date_format) - datetime0).days for date in df.columns[4:]] 
    df_country = df.loc[df['Country/Region'] == country]
    values = [value for value in df_country.iloc[0][4:]]
    return time, values

def extract_country_data2(df, country):
    df_by_country = df.drop(columns=['Lat', 'Long']).groupby(['Country/Region']).sum()
    dates = df_by_country.loc[country].index
    values = df_by_country.loc[country].values
    date_format = '%m/%d/%y'
    datetime0 = datetime.strptime(dates[0], date_format)
    time = [(datetime.strptime(date, date_format) - datetime0).days for date in dates] 
    return time, values



def extract_confirmed_deceased(country, population):
    df_confirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    time_confirmed, confirmed = extract_country_data2(df_confirmed, country)
    df_deceased = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    time_deceased, deceased =  extract_country_data2(df_deceased, country)
    limit = int(population/1e6)
    days_since_day0 = sum([x > limit for x in confirmed])
    offset = len(confirmed) - days_since_day0 - 10

    daily_confirmed = [x2 - x1 for x1, x2 in zip(confirmed, confirmed[1:])]
    daily_confirmed.insert(0, 0)
    daily_deceased = [x2 - x1 for x1, x2 in zip(deceased, deceased[1:])]
    daily_deceased.insert(0, 0)

    output = {
        'time': time_confirmed[offset:]-offset,
        'confirmed': confirmed[offset:],
        'deceased': deceased[offset:],
        'daily_confirmed': daily_confirmed[offset:],
        'daily_deceased': daily_deceased[offset:]

    }


    if len(time_confirmed) != len(time_deceased):
        raise AssertionError("Lengths of confirmed and deceased are not equal")
    else:
        return output


