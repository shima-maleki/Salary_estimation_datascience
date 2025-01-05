import pandas as pd
from pandas import DataFrame

class DataIngestion:
    def __init__(self, file_path: str): 
        self.file_path = file_path 

    def read_dataset(self):
        df = pd.read_csv(self.file_path)
        return df

    def clean_dataset(self):
        dataset = self.read_dataset()
        df = dataset[dataset['Salary Estimate'] != '-1']
        return df
    

    
    


if __name__ == "__main__":
    df_object= DataIngestion(file_path= 'data\df.csv')
    dataset = df_object.clean_dataset()
    print(dataset.head())
    


  

    
        