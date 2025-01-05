import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pickle

class ModelTraining:
    def __init__(self, file_path: str): 
        self.file_path = file_path 

    def read_dataset(self):
        df = pd.read_csv(self.file_path)
        return df

    def model(self):
        df = self.read_dataset()
        X = df.drop(columns='Average_salary')
        y = df['Average_salary']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state = 101)
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        pickle.dump(lr, open('Salary_Estimater.pkl' , 'wb'))