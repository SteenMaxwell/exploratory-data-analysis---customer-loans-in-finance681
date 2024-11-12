import pandas as pd

class SkewedData:
    def __init__(self, df):
        self.df = df

    def skew_check(self, threshold=1):
        numeric_df = self.df.select_dtypes(include=['number'])
        skewness = numeric_df.skew()
        skewed_columns = skewness[abs(skewness) > threshold].index
        return skewed_columns