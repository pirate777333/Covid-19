# IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# URL OF CSV
url_potvrdeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
url_umrli='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
url_oporavljeni='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv'

# LOAD DATA
try:
    df_potvrdeni=pd.read_csv(url_potvrdeni) # NEW CASES
    df_umrli=pd.read_csv(url_umrli) # DEATHS
    df_oporavljeni=pd.read_csv(url_oporavljeni) # RECOVERED

except:
    print('Something went wrong... URL problems')

# EXTRACT "CROATIA" ROW
df_potvrdeni_Croatia=df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia']
df_potvrdeni_Croatia_dates=df_potvrdeni_Croatia.iloc[:,4:]

# GRAPH - TOTAL CASES
# DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
x_cro_potvrdeni=df_potvrdeni_Croatia_dates.columns[-30:].tolist()

# DEFINING Y
y_cro_potvrdeni=[]
for i in df_potvrdeni_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_potvrdeni.append(j)

plt.figure(figsize=(20,12))
plt.plot(x_cro_potvrdeni,y_cro_potvrdeni, marker='.')
plt.xticks(rotation='vertical')
plt.title('TOTAL NUMBER OF CONFIRMED CASES')
plt.grid()
plt.xticks(x_cro_potvrdeni[::2])
plt.show()


# GRAPH - DAILY CASES
# X IS THE SAME
# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
# COLUMNS FROM -31,-1
y_cro_potvrdeni2=[]
for i in df_potvrdeni_Croatia_dates.iloc[:,-31:-1].values:
    for j in i:
        y_cro_potvrdeni2.append(j)

# REVERSED LISTS        
yr=list(reversed(y_cro_potvrdeni))

yrc=list(reversed(y_cro_potvrdeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAA
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.figure(figsize=(20,12))
plt.plot(x_cro_potvrdeni,ny, marker='.')
plt.xticks(x_cro_potvrdeni[::2],rotation='vertical')
plt.title('CONFIRMED CASES - DAILY NUMBERS')
plt.grid()
plt.show()


##############################################################################################################################################################

df_umrli_Croatia=df_umrli.loc[df_umrli['Country/Region']=='Croatia']
df_umrli_Croatia_dates=df_umrli_Croatia.iloc[:,4:]

# GRAF - TOTAL DEATHS
# DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
x_cro_umrli=df_umrli_Croatia_dates.columns[-30:].tolist()

# DEFINING Y
y_cro_umrli=[]
for i in df_umrli_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_umrli.append(j)

plt.figure(figsize=(20,12))
plt.plot(x_cro_umrli,y_cro_umrli, marker='.', color='red')
plt.xticks(rotation='vertical')
plt.title('TOTAL NUMBER OF DEATHS')
plt.grid()
plt.xticks(x_cro_umrli[::2])
plt.show()


# GRAPH - DAILY CASES
# X REMAINS THE SAME
# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
y_cro_umrli2=[]
for i in df_umrli_Croatia_dates.iloc[:,-31:-1].values:
    for j in i:
        y_cro_umrli2.append(j)

# REVERSED 2 LISTS        
yr=list(reversed(y_cro_umrli))
yrc=list(reversed(y_cro_umrli2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.figure(figsize=(20,12))
plt.scatter(x_cro_umrli,ny, marker='.', color='red')
plt.xticks(x_cro_umrli[::2],rotation='vertical')
plt.title('DAILY NUMBER OF DEATHS')
plt.grid()
plt.show()


##############################################################################################################################################################

df_oporavljeni_Croatia=df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia']
df_oporavljeni_Croatia_dates=df_oporavljeni_Croatia.iloc[:,4:]

# GRAPH - TOTAL RECOVERED
# DEFINING X, LAST 30 COLUMNS, TO THE LIST (NAMES OF COLUMNS ARE DATES)
x_cro_oporavljeni=df_oporavljeni_Croatia_dates.columns[-30:].tolist()

# DEFINING Y
y_cro_oporavljeni=[]
for i in df_oporavljeni_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_oporavljeni.append(j)

plt.figure(figsize=(20,12))
plt.plot(x_cro_oporavljeni,y_cro_oporavljeni, marker='.', color='green')
plt.xticks(rotation='vertical')
plt.title('NUMBER OF RECOVERED - TOTAL')
plt.grid()
plt.xticks(x_cro_oporavljeni[::2])
plt.show()


# GRAPH - DAILY CASES
# X REMAINS THE SAME
# DEFINING Y - DIFFERENCE OF THE LAST 30 COLUMNS AND COLUMNS FROM -31,-1
y_cro_oporavljeni2=[]
for i in df_oporavljeni_Croatia_dates.iloc[:,-31:-1].values:
    for j in i:
        y_cro_oporavljeni2.append(j)

# REVERSED 2 LISTS        
yr=list(reversed(y_cro_oporavljeni))
yrc=list(reversed(y_cro_oporavljeni2))

# TO ARRAY
yra=np.array(yr)
yrca=np.array(yrc)

# DIFFERENCE 2 ARRAYAS
ny=yra-yrca

# TO LIST, REVERSED
ny=list(reversed(ny))

plt.figure(figsize=(20,12))
plt.plot(x_cro_oporavljeni,ny, marker='.', color='green')
plt.xticks(x_cro_oporavljeni[::2],rotation='vertical')
plt.title('DAILY NUMBER OF RECOVERED')
plt.grid()
plt.show()


##############################################################################################################################################################

# GRAPH - ACTIVE CASES LAST 30 DAYS
# DEFINING X (SAME)
x_cro_oporavljeni=df_oporavljeni_Croatia_dates.columns[-30:].tolist()

# DEFINING Y : NEW CASES - DEATHS - RECOVERED
y_cro_potvrdeni=[] # NEW CASES
for i in df_potvrdeni_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_potvrdeni.append(j)
        
y_cro_oporavljeni=[] # DEATHS
for i in df_oporavljeni_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_oporavljeni.append(j)

y_cro_umrli=[] # RECOVERED
for i in df_umrli_Croatia_dates.iloc[:,-30:].values:
    for j in i:
        y_cro_umrli.append(j)


a=np.array(y_cro_potvrdeni)
b=np.array(y_cro_oporavljeni)
c=np.array(y_cro_umrli)
y=a-b-c

plt.figure(figsize=(20,12))
plt.plot(x_cro_oporavljeni,y, marker='.', color='orange')
plt.xticks(rotation='vertical')
plt.title('ACTIVE CASES')
plt.grid()
plt.xticks(x_cro_oporavljeni[::2])
plt.show()
