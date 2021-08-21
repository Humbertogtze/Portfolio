import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def myLogisticRegresson(df):
    cleandf = df.applymap(lambda x: 1 if x in ("t", "l", "n", "won") else 0) #maps to 0 or 1 correspondingly
    feature_cols = cleandf.columns[:-1]
    x = cleandf[feature_cols] #selects all but the last column as an array
    y = cleandf[cleandf.columns[-1]]
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
    logreg = LogisticRegression(max_iter = len(X_train))
    logreg.fit(X_train, y_train)
    y_pred = logreg.predict(X_test)
    MatrixVisualization(y_test, y_pred)

def MatrixVisualization(y_test, y_pred):
    matrix = confusion_matrix(y_test, y_pred)
        #this returns the confusion matrix in array form
    class_names = [0,1] #0 means no, 1 means yes (that the data classified)
    fig, ax = plt.subplots()
        #this method is to plot
    tick_marks = np.arange(len(class_names))
        #passes the class for the plotting
    plt.xticks(tick_marks, class_names)
    plt.yticks(tick_marks, class_names)

    sns.heatmap(pd.DataFrame(matrix), annot = True, cmap = 'Blues_r', fmt = 'g')
        #this creates the heat map for our plot
    ax.xaxis.set_label_position('top')
        #this tells the computer where to put the plot label
    plt.tight_layout()
        #generates the layout
    plt.title('Confusion matrix', y = 1.1)
        #selects the title of the plot and its position
    plt.ylabel('Actual information (test information)')
    plt.xlabel('Generated information (prediction)')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv(r'C:\Users\humbe\OneDrive\Desktop\Data Science\Machine learning projects\Machine learning projects datasets\kr-vs-kp.csv')
    myLogisticRegresson(df)