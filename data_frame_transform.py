from data_frame_info import DataFrameInfo
import pandas as pd
import numpy as np


class DataFrameTransform:
    def __init__(self, df, threshold=0.1):
        self.df = df
        self.threshold = threshold


    def drop_high_null_columns(self):
        null_info = DataFrameInfo(self.df)
        null_percentage = null_info.null_value_count(as_percentage=True)
        
        columns_to_drop = null_percentage[null_percentage > self.threshold * 100].index
        self.df.drop(columns=columns_to_drop, inplace=True)
        
        return self.df
    

    def impute_missing_values(self):
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                if self.df[col].isnull().sum() > 0:
                    skewness = self.df[col].skew()

                    if abs(skewness) > 1:
                        self.df[col] = self.df[col].fillna(self.df[col].median())
                    else:
                        self.df[col] = self.df[col].fillna(self.df[col].mean())
            
            else:
                if self.df[col].isnull().sum() > 0:
                    self.df[col] = self.df[col].fillna(self.df[col].mode()[0])

        return self.df
    

    def transform_skewed_columns(self, skewed_columns):
        for col in skewed_columns:
            log_transformed = self.df[col].apply(lambda i: np.log(i) if i > 0  else 0)
            self.df[col] = log_transformed

        return self.df
            