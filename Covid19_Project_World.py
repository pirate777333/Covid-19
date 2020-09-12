# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# URL
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# IMPORT DATA
try:
    df_potvrdeni=pd.read_csv(url_potvrdeni)
    df_umrli=pd.read_csv(url_umrli)
    df_oporavljeni=pd.read_csv(url_oporavljeni)

except:
    print('Something went wrong... URL problems')


# GROUP THE DATA
# COLUMN Country/Region BECOMES INDEX

# NEW CASES
df_grupirano_potvrdeni=df_potvrdeni.groupby('Country/Region').sum()
df_grupirano_potvrdeni_dates=df_grupirano_potvrdeni.iloc[:,2:]

# DEATHS
df_grupirano_umrli=df_umrli.groupby('Country/Region').sum()
df_grupirano_umrli_dates=df_grupirano_umrli.iloc[:,2:]

# RECOVERED
df_grupirano_oporavljeni=df_oporavljeni.groupby('Country/Region').sum()
df_grupirano_oporavljeni_dates=df_grupirano_oporavljeni.iloc[:,2:]

# INPUT COUNTRY
drzava=input('Input name of the Country:  ')
drzava=drzava.lower()
drzava=drzava.title()
print('Your Country:  ' + drzava)

# SEARCH FOR INPUT IN DATA 
try:
    df_drzavni_potvrdeni=df_grupirano_potvrdeni_dates.loc[drzava].to_frame()
    df_drzavni_umrli=df_grupirano_umrli_dates.loc[drzava].to_frame()
    df_drzavni_oporavljeni=df_grupirano_oporavljeni_dates.loc[drzava].to_frame()

except:
    print("Something went wrong. Name of the country is wrong or it doesn't exist")

##########################################################################################

# NEW CASES

# X 
x_drzavni_potvrdeni=df_drzavni_potvrdeni.index[-30:].tolist()

# Y LAST 30 DAYS
y_drzavni_potvrdeni=[]
for i in df_drzavni_potvrdeni.iloc[-30:].values:
    for j in i:
        y_drzavni_potvrdeni.append(j)

y_drzavni_potvrdeni2=[]
for i in df_drzavni_potvrdeni.iloc[-31:-1].values:
    for j in i:
        y_drzavni_potvrdeni2.append(j)


# REVERSED 2 DEFINED LISTS       
yr=list(reversed(y_drzavni_potvrdeni))
yrc=list(reversed(y_drzavni_potvrdeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.figure(figsize=(20,18))
plt.subplot(2,2,1)


plt.plot(x_drzavni_potvrdeni,ny, marker='.')
plt.xticks(rotation='vertical')
plt.title('Daily number of new confirmed cases')
plt.grid()
plt.xticks(x_drzavni_potvrdeni[::2]+['Tomorrow'])


##########################################################################################

# DEATHS

# X 
x_drzavni_umrli=df_drzavni_umrli.index[-30:].tolist()

# Y 
y_drzavni_umrli=[]
for i in df_drzavni_umrli.iloc[-30:].values:
    for j in i:
        y_drzavni_umrli.append(j)

y_drzavni_umrli2=[]
for i in df_drzavni_umrli.iloc[-31:-1].values:
    for j in i:
        y_drzavni_umrli2.append(j)


# REVERSED 2 DEFINED LISTS       
yr=list(reversed(y_drzavni_umrli))
yrc=list(reversed(y_drzavni_umrli2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.subplot(2,2,2)

plt.scatter(x_drzavni_umrli,ny, marker='.', color='red')
plt.xticks(rotation='vertical')
plt.title('Daily number of deaths')
plt.grid()
plt.xticks(x_drzavni_potvrdeni[::2]+['Tomorrow'])


##########################################################################################

# RECOVERED


# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-30:].tolist()

# Y 
y_drzavni_oporavljeni=[]
for i in df_drzavni_oporavljeni.iloc[-30:].values:
    for j in i:
        y_drzavni_oporavljeni.append(j)

y_drzavni_oporavljeni2=[]
for i in df_drzavni_oporavljeni.iloc[-31:-1].values:
    for j in i:
        y_drzavni_oporavljeni2.append(j)


# REVERSED 2 DEFINED LISTS       
yr=list(reversed(y_drzavni_oporavljeni))
yrc=list(reversed(y_drzavni_oporavljeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.subplot(2,2,3)

plt.plot(x_drzavni_oporavljeni,ny, marker='.', color='green')
plt.xticks(rotation='vertical')
plt.title('Daily number of recovered')
plt.grid()
plt.xticks(x_drzavni_potvrdeni[::2]+['Tomorrow'])



##########################################################################################

# ACTIVE CASES

# X 
x_drzavni_oporavljeni=df_drzavni_oporavljeni.index[-30:].tolist()

# Y - CONFIRMED - DEATHS - RECOVERED
a=np.array(y_drzavni_potvrdeni)
b=np.array(y_drzavni_umrli)
c=np.array(y_drzavni_oporavljeni)
y=a-b-c

plt.subplot(2,2,4)

plt.plot(x_drzavni_oporavljeni,y, marker='.', color='orange')
plt.xticks(rotation='vertical')
plt.title('Daily number of active cases')
plt.grid()
plt.xticks(x_drzavni_potvrdeni[::2]+['Tomorrow'])
plt.tight_layout()
plt.show()
