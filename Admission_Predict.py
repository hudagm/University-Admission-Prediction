import pandas as pd
import numpy as np
# import matplotlib.pyplot as pyplot
# import seaborn as sns

data = pd.read_csv("unidata.csv")
admission_df = data.drop('Serial No.', axis=1)

X = admission_df.drop(columns =['Chance of Admit '])
y = admission_df['Chance of Admit ']

X = np.array(X)
y = np.array(y)

y = y.reshape(-1,1)

from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)

scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)

### Linear Regressor

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score

LinearRegression_model = LinearRegression()
LinearRegression_model.fit(X_train, y_train)

import pickle
pickle.dump(LinearRegression_model, open('unimodel.pkl', 'wb'))

student_1 = np.array([340,120,3,3,3,9.8,1], ndmin=2)
prediction_1 = LinearRegression_model.predict(student_1)




##accuracy
# LinearRegression_accuracy = LinearRegression_model.score(X_test, y_test)
# print(LinearRegression_accuracy)

