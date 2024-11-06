import pandas as pd

class DataFrameInfo:
    def __init__(self, df):
        self.df = df
    
    def dtype_for_columns(self):
        '''Returns the dtype for each column in the DataFrame.'''
        column_dtypes = self.df.dtypes
        return column_dtypes

    def shape_of_data(self):
        '''Returns the shape of the data: a tuple (rows, columns).'''
        shape = self.df.shape
        return shape

    def describe_columns(self, columns):
        '''Returns a description of each column in a DataFrame.'''
        described_columns = {}
        for col in columns:
            described_columns[col] = self.df[col].describe()
        return described_columns

    def extract_statistical_values(self):
        '''Extracts and returns mean, median and standard deviation for numeric columns.'''
        statistics = {
            "mean": self.df.mean(numeric_only=True),
            "median": self.df.median(numeric_only=True),
            "std_dev": self.df.std(numeric_only=True)
        }
        print("Statistics:\n")
        return statistics

    def distinct_values_categorical_count(self):
        '''Returns the distinct number of unique items in the categorical columns.'''
        categorical_columns = self.df.select_dtypes(include='category').columns
        distinct_counts = {col: self.df[col].nunique() for col in categorical_columns}
        return distinct_counts

    def null_value_count(self, as_percentage=False):
        '''Returns either the null count as a percentage or a number depending on the argument used.
           Parameter:
           ---------
           as_percentage=False : so can decide if method should return a percentage or number
                - For a percentage, include 'as_percentage = True' as an argument
                - For the sum number, no argument needed
        '''
        if as_percentage:
            null_counts = self.df.isnull().sum()/len(self.df) * 100  
        else:
            null_counts = self.df.isnull().sum()  
        return null_counts