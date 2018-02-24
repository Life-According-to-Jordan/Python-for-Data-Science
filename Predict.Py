'''
Install Dependencies:
    [pip install csv]
    [pip install numpy]
    [pip install scikit-learn]
    [pip install matplot lib]

csv allows us to read csv files
numpy will allow us to perform calculations on our data
scikit-learn will allow us to build a predictive model
matplotlib will allow us to plot our data
'''

#Import Libraries 
import csv
import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

dates = []
prices = []

#I downloaded my data from yahoo and Saraj downloaded his from Google. A setting had changed and I could not replicate his code precisely.
#filename should be the name of the csv downloaded
def get_data(aapl):
        with open(aapl, 'r') as csvfile:
            next(csvFileReader)
            for row in csvFileReader:
            #append allows us to add an item to the end of our list
            #split will remove the dashes between our values
                dates.append(int(row[0].split('/')[0]))
            #float will allow us to be more precise in our later calculations
                prices.append(float(row[1]))
            return

#build predictive model and plot it
#n by 1 matrix
def predict_prices(dates, prices, x):
    dates = np.reshape(dates,(len(dates),1))
    #support vector regression, type = linear, error = 1e3
    svr_lin = SVR(kernal='linear', c=1e3)
    #polynomial
    svr_poly = SVR(kernal='poly', c=1e3, degree =2)
    #gamma defines how far too far is
    svr_rbf = SVR(kernal='rbf', c=1e3, gamma=0.1)
    #Next, fit and train each model
    svr_rbf.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    #Time to plot our data!
    #color and label are pretty generic and we should all understand that
    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear Model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression')
    plt.legend()
    ply.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data(AAPL.csv)

#Unsure why we used 29 here
predicted.price = predict_price(dates, prices, 29)

print(predicted.price)
