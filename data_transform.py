import pandas as pd


class DataTransform:
    def __init__(self, df):
        self.df = df


    def date_conversion_to_datetime(self, date_columns):
        for col in date_columns:
            self.df[col] = pd.to_datetime(self.df[col], format='%b-%Y', errors='coerce')
        return self.df
    

    def set_string_columns(self, columns):
        for col in columns:
            self.df[col] = self.df[col].astype('string')
        return self.df
    

    def categorical_conversion(self, columns):
        for col in columns:
            self.df[col] = self.df[col].astype('category')
        return self.df
    

    def set_categorical_columns(self):
        categorical_columns = [
            'grade', 'sub_grade', 'employment_length', 'home_ownership', 
            'verification_status', 'loan_status', 'payment_plan', 
            'purpose', 'application_type', 'term', 'policy_code'
            ]
        
        self.categorical_conversion(categorical_columns)
        return self.df
    

    def transform(self):
        self.date_conversion_to_datetime(['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date'])
        self.set_string_columns(['id', 'member_id'])
        self.set_categorical_columns()

        return self.df