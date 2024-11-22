'''pandas is used in this file specifically for conversion to datetime'''
import pandas as pd


class DataTransform:
    '''
    DataTransform class converts columns in a DataFrame to specific dtypes
    depending on the data in each column.

    Methods:
    -------
    date_conversion_to_datetime()
        converts specific columns to 'datetime' dtype.

    set_string_columns()
        Converts specific columns to 'string' dtype.

    categorical_conversion()
        Converts specified columns given to 'category' dtype.
    
    set_categorical_conversion()
        Columns containing categorical data given and converted to dtype.

    transform()
        transforms all specified columns in the DataFrame by calling each method.
    '''

    def __init__(self, df):
        '''
        Attributes:
        ----------
        df: pd.DataFrame
            The DataFrame containing the dataset to be analysed and visualised.
        '''
        self.df = df


    def date_conversion_to_datetime(self, date_columns: list):
        '''This method converts specific columns dtype in a DataFrame to 'datetime'.
        
        Parameter:
        ----------
        date_columns: list
            a list of columns to be converted to 'datetime' dtype.
        '''
        for col in date_columns:
            self.df[col] = pd.to_datetime(self.df[col], format='%b-%Y', errors='coerce')
        return self.df


    def set_string_columns(self, string_columns: list):
        '''This method converts specific columns dtype in a DataFrame to 'string'.

        Parameter:
        ----------
        string_columns: list
            a list of columns to be converted to 'string' dtype.
        '''
        for col in string_columns:
            self.df[col] = self.df[col].astype('string')
        return self.df


    def categorical_conversion(self, category_columns: list):
        '''This method converts specific columns dtype in a DataFrame to 'category'.

        Parameters:
        ----------
        category_columns: list
            a list of columns to be converted to 'category' dtype.
        '''
        for col in category_columns:
            self.df[col] = self.df[col].astype('category')
        return self.df


    def set_categorical_columns(self):
        '''Categorical columns are provided so the conversion to 'category' dtype can occur.'''
        categorical_columns = [
            'grade', 'sub_grade', 'employment_length', 'home_ownership', 
            'verification_status', 'loan_status', 'payment_plan', 
            'purpose', 'application_type', 'term', 'policy_code'
            ]

        self.categorical_conversion(categorical_columns)
        return self.df


    def transform(self):
        '''
        Calls all other methods in the DataTransform Class so only one method 
        is needed to make all conversions.
        '''
        self.date_conversion_to_datetime(['issue_date', 'earliest_credit_line', 'last_payment_date',
                                         'next_payment_date', 'last_credit_pull_date'])
        self.set_string_columns(['id', 'member_id'])
        self.set_categorical_columns()

        return self.df
