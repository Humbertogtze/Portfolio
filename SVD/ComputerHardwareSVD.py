import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Data_cleaner(df):
    df.drop(columns = ['Model Name', 'ERP'], inplace = True) 
        #drops the irrelevant data and an estimation column, which is the whole purpose of the regression

    df = df.sample(frac=1).reset_index(drop=True)
        #randomly samples the rows to avoid overfitting

    dummydata = pd.get_dummies(df, columns=['vendor name'])
        #gets dummy variables for the column with the vendor name info

    X = np.array(dummydata, dtype='float')

    vendors = pd.unique(df['vendor name'])
    X = np.roll(X, len(vendors), axis=1)
        #order the columns such that dummy values are on the front

    b = X[:,-1] #Published relative performance
    A = X[:,:-1] #All other data

    A = np.pad(X,[(0,0),(0,1)],mode='constant',constant_values=1) 
        #pads a list of 1's so the line can go off the origin, also, converts the dataframe into a numpy ndarray so we can perform the svd

    SVD(b, A, X)

def SVD(b ,A, X):

    n = 167

    btrain = b[:n]
    Atrain = A[:n]

    btest = b[n:]
    Atest = A[n:]
        #separates data into training and testing data

    U, S, VT = np.linalg.svd(Atrain,full_matrices=0)
    x = VT.T @ np.linalg.inv(np.diag(S)) @ U.T @ btrain
        #solves for Ax = b using the SVD
    
    #The next part is for plotting

    fig = plt.figure()

    ax2 = fig.add_subplot(1, 1, 1)
    plt.plot(btest, color='k', linewidth=2, label='True performance') # True relationship
    plt.plot(Atest@x, 'o-', color='y', linewidth=1, markersize=6, label='Regression')
    plt.xlabel("Different CPU's performance")
    plt.ylabel("Relative performance")
    plt.legend()

    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('computerHardwareDataSet.csv', names=['vendor name', 'Model Name', 'MYCT', 'MMIN', 'MMAX', 'CACH', 'CHMIN', 'CHMAX', 'PRP', 'ERP']) #loads data set and assigns column name
    Data_cleaner(df)
