'''
Imports the DataFrameInfo class and key libraries for data analysis.

Modules:
--------
- DataFrameInfo: Custom class to extract information from pandas DataFrames.
- pandas (pd): Essential library for data manipulation and analysis.
- numpy (np): Library for numerical operations, often used alongside pandas for data handling.
- scipy.stats: includes Box-Cox transformation for normalising data.
'''

from data_frame_info import DataFrameInfo
import pandas as pd
import numpy as np
from scipy.stats import boxcox


class DataFrameTransform:
    """
    A class for performing various transformations on a pandas DataFrame, including handling 
    missing values, skewed data, outliers, and highly correlated columns.
    
    Parameters:
    ----------
    df: pd.DataFrame
        The DataFrame to be transformed.
    threshold: float, optional, default=0.1
        Threshold for dropping columns based on their null value percentage.
    """

    def __init__(self, df, threshold=0.1):
        '''
        Parameters:
        ----------
        df: pd.DataFrame
            The DataFrame to be transformed.
        
        threshold: float, optional, default=0.1
            Threshold for dropping columns based on their null value percentage.
        '''
        self.df = df
        self.threshold = threshold


    def drop_high_null_columns(self):
        """
        Drops columns from the DataFrame with a high percentage of null values based on 
        the threshold.
        
        Returns:
        -------
        pd.DataFrame
            The DataFrame with columns dropped where null values exceed the threshold percentage.
        """
        null_info = DataFrameInfo(self.df)
        null_percentage = null_info.null_value_count(as_percentage=True)

        columns_to_drop = null_percentage[null_percentage > self.threshold * 100].index
        self.df.drop(columns=columns_to_drop, inplace=True)

        return self.df


    def impute_missing_values(self):
        """
        Imputes missing values in the DataFrame. Numerical columns with high skew are filled 
        with the median; other numerical columns are filled with the mean. 
        Categorical columns are filled with the mode.
        
        Returns:
        -------
        pd.DataFrame
            The DataFrame with missing values imputed.
        """
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


    def best_transform_skewed_columns(self, skewed_columns):
        """
        Applies a logarithmic transformation to specified skewed columns to reduce skewness.
        
        Parameters:
        ----------
        skewed_columns: list of str
            List of column names in the DataFrame that are skewed and need transformation.
        
        Returns:
        -------
        pd.DataFrame
            The DataFrame with transformed skewed columns.
        """
        
        def calculate_skewness(col_data, method):
            """Helper function to apply a transformation and calculate skewness."""
            if method == 'log':
                transformed = col_data.apply(lambda x: np.log(x) if x > 0 else 0)
            elif method == 'sqrt':
                transformed = col_data.apply(lambda x: np.sqrt(x) if x >= 0 else 0)
            elif method == 'boxcox':
                if (col_data > 0).all():
                    transformed, _ = boxcox(col_data)
                    transformed = pd.Series(transformed)
                else:
                    return float('inf')
            return abs(transformed.skew())

        for col in skewed_columns:
            col_data = self.df[col]
            original_skew = abs(col_data.skew())

            transformations = ['log', 'sqrt', 'boxcox']
            skew_results = {}
            for method in transformations:
                skew_results[method] = calculate_skewness(col_data, method)

            best_method = min(skew_results, key=skew_results.get)
            best_skew = skew_results[best_method]

            if best_skew < original_skew:
                if best_method == 'log':
                    self.df[col] = col_data.apply(lambda x: np.log(x) if x > 0 else 0)
                elif best_method == 'sqrt':
                    self.df[col] = col_data.apply(lambda x: np.sqrt(x) if x >= 0 else 0)
                elif best_method == 'boxcox':
                    self.df[col], _ = boxcox(col_data)

        return self.df


    def remove_outliers(self, columns=None, threshold=1.5):
        """
        Removes outliers from the specified columns in the DataFrame using the IQR method.
        
        Parameters:
        ----------
        columns: list of str, optional
            List of column names to check for outliers. If None, all numeric columns are used.
        threshold: float, optional, default=1.5
            The threshold multiplier for the IQR to define the lower and upper bounds.
        
        Returns:
        -------
        pd.DataFrame
            The DataFrame with outliers removed from specified columns.
        """
        if columns is None:
            columns = self.df.select_dtypes(include='number').columns
        else:
            columns = [col for col in columns if col in self.df.select_dtypes(include='number').columns]

        for col in columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 -Q1
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR

            self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]

        return self.df


    def remove_high_correlation_columns(self, columns_to_remove):
        """
        Removes specified columns from the DataFrame, typically used to eliminate 
        highly correlated columns.
        
        Parameters:
        ----------
        columns_to_remove: list of str
            List of column names to be removed from the DataFrame.
        
        Returns:
        -------
        pd.DataFrame
            The DataFrame with specified columns removed.
        """
        columns_to_remove = [col for col in columns_to_remove if col in self.df.columns]

        self.df = self.df.drop(columns=columns_to_remove)

        return self.df
