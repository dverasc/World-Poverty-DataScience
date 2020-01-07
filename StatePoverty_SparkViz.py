

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd

from pyspark.sql import SparkSession

from pyspark.sql.functions import countDistinct,avg,stddev





#Initiate spark session and read in the file, in the real code I used the full file path since they were in different directories but obviously I won't show my path here

spark = SparkSession.builder.config("spark.sql.warehouse.dir", "file:///C:/temp").appName("aggs").getOrCreate()

df = spark.read.csv(r'Poverty-by-State.csv',inferSchema=True,header=True)

#df.show()







#Here we are creating a new object with just the states in the southeast, the full file had all 50 states across the time period

df_FL = df.filter( (df['State'] == 'Florida') | (df['State'] == 'Alabama') | (df['State'] == 'Georgia') | (df['State'] == 'Arkansas') | (df['State'] == 'Louisiana') | (df['State'] == 'Mississippi') | (df['State'] == 'North Carolina') | (df['State'] == 'South Carolina') | (df['State'] == 'Tennessee') )

                 #   )



#Here we convert the spark data object to a pandas dataframe

df_pandas = df_FL.toPandas()





#the use of pivot here is what lets the plotting across each state and year with the percentage rate as our quantitative values

pivot_df = df_pandas.pivot(index='Year', columns ='State', values='Percent')

pivot_df.plot.line(figsize=(15,15))



#setting title and labels

plt.title('Poverty Percent Rates over Time in Southeast USA')

plt.xlabel('Year')

plt.ylabel('Percent Rate')













#groupeddf = df_pandas['Percent'].groupby([df_pandas['State']])



#df_pandas.head(20)





#df_pandas.plot(x='Year',y='Percent',kind='line')

#plt.show()
