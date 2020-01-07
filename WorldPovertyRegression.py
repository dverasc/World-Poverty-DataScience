##import needed libraries/packages
##matplotlib inline is used for jupyter notebooks

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#open world poverty file and set it to dataframe variable
df = pd.read_csv(r'C:\Users\dveras\Downloads\countries.csv')

##preview dataframe
df.head()

##explore data using different packages
sns.pairplot(df)

#explore comparison between life expectancy and population
sns.lmplot(y='lifeExpectancy',x='population',data=df)


#create dataframe for just the year 1972
is1972 = df['year'] == 1972
cleanframe = df[is1972]
print(cleanframe.head())


##comparison between life expectancy and gdp per capita, but only year 1972
sns.lmplot(y='lifeExpectancy',x='gdpPerCapita',data=cleanframe)

##linear regression exploring relationship between life expectancy, population, and year versus the gdpPerCapita
X = df[['lifeExpectancy','population','year']]
y = df['gdpPerCapita']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size= 0.3,random_state=101)

from sklearn.linear_model import LinearRegression

lm = LinearRegression()
lm.fit(X_train,y_train)

print(lm.coef_)


##evaluate coefficients
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
coeff_df

##explore predictions using scatterplot
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)

##evaluate predictions using distribution
sns.distplot((y_test-predictions),bins=50);

##print summmary statistics
from sklearn import metrics

print('MAE: ', metrics.mean_absolute_error(y_test,predictions))
print('MSE: ', metrics.mean_squared_error(y_test,predictions))
print('RMSE: ', np.sqrt(metrics.mean_squared_error(y_test,predictions)))
