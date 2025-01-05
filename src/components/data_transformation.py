import pandas as pd
from pandas import DataFrame
from src.utils.helper import title_organizer, sat


class DataTransformation:
    def __init__(self, file_path: str): 
        self.file_path = file_path 

    def read_dataset(self):
        df = pd.read_csv(self.file_path)
        return df

    def calculate_average_salary(self):
        df = self.read_dataset() 
        df = df[~df['Salary Estimate'].str.contains('Per Hour')]
        df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.replace('$', ' '))
        df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.replace('K', ' '))
        df['Salary Estimate'] = df['Salary Estimate'].apply(lambda x: x.split())
        df['Min_salary'] = df['Salary Estimate'].apply(lambda x: x[0])
        df['Max_salary'] = df['Salary Estimate'].apply(lambda x: x[2])
        df['Min_salary'] = df['Min_salary'].apply(lambda x:int(x))
        df['Max_salary']=df['Max_salary'].astype(int)
        df['Average_salary'] = (df.Min_salary + df.Max_salary)/2
        return df
    

    def remove_non_usa_states(self):
        df = self.calculate_average_salary()
        df['State'] = df['Location'].apply(lambda x: x.split()[-1])
        df = df[df.State != 'Kingdom'] 
        return df
    
    def create_title_organisor(self):
        df = self.remove_non_usa_states()
        df['Job Title'] = df['Job Title'].apply(title_organizer)
        df = df[df['Rating']!=-1]
        return df
    

    def get_tranformed_data(self):
        df = self.create_title_organisor()
        df = df[['Job Title', 'Rating', 'Average_salary', 'State']]
        return df

    def feature_engineering(self):
        df = self.get_tranformed_data()
        preprocessed_df = pd.get_dummies(df, columns=['Job Title','State'])
        preprocessed_df['Satisfaction'] = preprocessed_df['Average_salary'].apply(sat)
        return preprocessed_df

if __name__ == "__main__":
    df_object= DataTransformation(file_path= 'data\df.csv')
    dataset = df_object.feature_engineering()
    print(dataset.head())








