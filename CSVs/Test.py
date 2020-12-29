import pandas as pd
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#weather = pd.read_csv('London Only.csv')
weather = pd.read_csv('London Only2.csv')
weather.head() # look at top 5 entries as very big file

print(weather.info()) # print out the columns and their types and number in reries format
weather.head() # then look at the head of the data frame

axs = plt.subplots(1, 1)

#sns.scatterplot(x = weather['Year'], y = weather['Moving Norm Avg.(7)'], hue = weather['City'])
sns.scatterplot(x='Year', y='Norm. Mov. Avg. (per 7)', hue = 'City', data=weather)
plt.savefig('London-ScatterPlot.svg')
plt.savefig('London-ScatterPlot.png', transparent=True, dpi=300)

sns.lineplot(x = 'Year', y = 'Norm. Mov. Avg. (per 7)', hue = 'City', data=weather)
plt.savefig('London-LinePlot.pdf')