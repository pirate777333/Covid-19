# IMPORT LIBRARIES
import pandas as pd
import numpy as np
from bokeh.plotting import ColumnDataSource, figure, output_file, show
import datetime
from bokeh.layouts import column, row
from pyproj import Proj, transform
from bokeh.tile_providers import get_provider, Vendors
from bokeh.models import HoverTool
import ipywidgets
from bokeh.io import push_notebook
from bokeh.models import Range1d
from bokeh.models.widgets import Panel, Tabs

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

# LIST OF COLUMNS
stupci=df_potvrdeni.columns[-8:].to_list() #25,26,27,28,29,30,31

# BAR DATA, LAST 7 DAYS - CONFIRMED CASES CROATIA
x_bar_data=[stupci[0],stupci[1],stupci[2],stupci[3],
            stupci[4],stupci[5],stupci[6]]
y_bar_data=[df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[1]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[0]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[2]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[1]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[3]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[2]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[4]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[3]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[5]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[4]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[6]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[5]].values[0],
            df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[7]].values[0]-
      df_potvrdeni.loc[df_potvrdeni['Country/Region']=='Croatia', stupci[6]].values[0]]

bar_chart_interactive=figure(x_range=x_bar_data, plot_height=500, plot_width=500)
bar_ipyw=bar_chart_interactive.vbar(x_bar_data, top=y_bar_data, color='green', width=0.5)
bar_chart_interactive.y_range=Range1d(0,400)

# BAR DATA, LAST 7 DAYS - DEATHS CROATIA
x_bar_data1=[stupci[0],stupci[1],stupci[2],stupci[3],
            stupci[4],stupci[5],stupci[6]]
y_bar_data1=[df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[1]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[0]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[2]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[1]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[3]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[2]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[4]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[3]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[5]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[4]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[6]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[5]].values[0],
            df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[7]].values[0]-
      df_umrli.loc[df_umrli['Country/Region']=='Croatia', stupci[6]].values[0]]

bar_chart_interactive1=figure(x_range=x_bar_data1, plot_height=500, plot_width=500)
bar_ipyw1=bar_chart_interactive1.vbar(x_bar_data1, top=y_bar_data1, color='green', width=0.5)
bar_chart_interactive1.y_range=Range1d(0,10)

# BAR DATA, LAST 7 DAYS - RECOVERED CROATIA
x_bar_data2=[stupci[0],stupci[1],stupci[2],stupci[3],
            stupci[4],stupci[5],stupci[6]]
y_bar_data2=[df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[1]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[0]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[2]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[1]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[3]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[2]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[4]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[3]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[5]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[4]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[6]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[5]].values[0],
            df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[7]].values[0]-
      df_oporavljeni.loc[df_oporavljeni['Country/Region']=='Croatia', stupci[6]].values[0]]

bar_chart_interactive2=figure(x_range=x_bar_data2, plot_height=500, plot_width=500)
bar_ipyw2=bar_chart_interactive2.vbar(x_bar_data2, top=y_bar_data2, color='green', width=0.5)
bar_chart_interactive2.y_range=Range1d(0,400)

# CREATE PANELS
first=Panel(child=row(bar_chart_interactive), title='Potvrdeni')
second=Panel(child=row(bar_chart_interactive1), title='Umrli')
third=Panel(child=row(bar_chart_interactive2), title='Oporavljeni')

# CREATE TABS FOR PANELS, OUTPUT, SHOW IT
tabs=Tabs(tabs=[first, second,third])
output_file('tabbed.html')

show(tabs)
