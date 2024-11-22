class DataFrameInfo:
    '''
    DataFrameInfo class has a range of methods for extracting information out of 
    a DataFrame. Use this class to gain information about the data.

    Methods:
    -------
    dtype_for_columns()
        returns dtype for each column in a DataFrame.

    shape_of_data()
        returns the shape of the DataFrame.

    describe_columns()
        returns a description of each column in a DataFrame.

    extract_statistical_values()
        Extracts and returns mean, median and standard deviation for numeric columns.

    distinct_values_categorical_count()
        Returns the distinct number of unique items in a categorical columns.

    null_value_counts()
        Returns either the null count as a percentage or a number.
    '''
    def __init__(self, df):
        '''
        Attributes:
        ----------
        df: pd.DataFrame
            The DataFrame containing the dataset to be analysed and visualised.
        '''
        self.df = df


    def dtype_for_columns(self):
        '''Returns the dtype for each column in the DataFrame.'''
        column_dtypes = self.df.dtypes
        return column_dtypes


    def shape_of_data(self):
        '''Returns the shape of the data; a tuple (rows, columns).'''
        shape = self.df.shape
        return shape


    def describe_columns(self, columns: list):
        '''Returns a description of each column in a DataFrame.
        
        Parameter:
        ----------
        columns: list of str
        A list of column names in the DataFrame to describe.
        
        Returns:
        -------
        described_columns: dict
            A dictionary where each key is a column name, and the value is a description 
            of that column.
        '''
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
           as_percentage=False: so can decide if method should return a percentage or number
                - For a percentage, include 'as_percentage = True' as an argument
                - For the sum number, no argument needed
        '''
        if as_percentage:
            null_counts = self.df.isnull().sum()/len(self.df) * 100
        else:
            null_counts = self.df.isnull().sum()
        return null_counts


    def skew_check(self, threshold=1):
        '''
        Identifies skewed columns based on a given skewness threshold.

        Parameter:
        ----------
        threshold : float or int, default=1
            The skewness value threshold. Columns with an absolute skewness
            greater than this threshold are identified as skewed and added 
            to the output list.
    
        Returns:
        -------
        skewed_columns : Index
            Index of column names in the DataFrame that have skewness values 
            exceeding the specified threshold.
        '''
        numeric_df = self.df.select_dtypes(include=['number'])
        skewness = numeric_df.skew()
        skewed_columns = skewness[abs(skewness) > threshold].index
        return skewed_columns
