'''
Imports essential libraries for data visualization, data manipulation, and numerical operations.

Modules:
--------
- seaborn (sns): Visualization library based on Matplotlib, used for statistical graphics.
- pandas (pd): Library for data manipulation and analysis, primarily for handling DataFrames.
- matplotlib.pyplot (plt): Core Matplotlib module for creating visualizations.
- numpy (np): Fundamental package for array computing, used for numerical operations on data.
'''

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class Plotter:
    ''' A class for visualising various data characteristics such as missing values, skewness,
    outliers, and correlation in a given DataFrame.
    '''
    def __init__(self, df):
        '''
        Attributes:
        ----------
        df: pd.DataFrame
            The DataFrame containing the dataset to be analysed and visualised.
        '''
        self.df = df


    def removal_of_null_visualised(self, original_data):
        '''
        Visualises the percentage of missing values in each column before and after 
        transformation. Creates a bar plot comparing the missing values in the original 
        dataset to the transformed dataset.

        Parameter:
        ----------
        original_data: pd.DataFrame
            The original dataset prior to any transformations or null value removal.
        '''
        original_null_percentage = original_data.isnull().mean() * 100
        new_null_percentage = self.df.isnull().mean() * 100

        null_data = pd.DataFrame({
            'Original': original_null_percentage,
            'Transformed': new_null_percentage
        }).melt(ignore_index=False, var_name='Dataset', value_name='Missing percentage')

        null_data = null_data[null_data['Missing percentage'] > 0]

        null_data.reset_index(inplace=True)
        null_data.rename(columns={'index': 'Column'}, inplace=True)

        plt.figure(figsize=(12, 8))
        sns.barplot(data=null_data, y='Column', x='Missing percentage',
                    hue='Dataset', palette='viridis')

        plt.title('Percentage of nulls comparison before and after transformation')
        plt.xlabel('Percentage of missing values')
        plt.ylabel('Column Name')
        plt.legend(title='Dataset', loc='upper right')

        plt.tight_layout()
        plt.show()


    def skew_plotted(self, skewed_columns):
        '''
        Plots a FacetGrid for the skewed columns in the DataFrame to visualise the 
        distribution and skewness of the data.

        Parameter:
        ----------
        skewed_columns: list of str
            List of column names identified as having significant skewness in their 
            distributions.
        '''
        skewed_data = self.df[skewed_columns]

        skewed_data_melted = skewed_data.melt(var_name='variable', value_name='value')

        g = sns.FacetGrid(skewed_data_melted, col='variable', col_wrap=3,
                          sharex=False, sharey=False)
        g = g.map(sns.histplot, 'value', kde=True)

        g.set_axis_labels('Value', 'Frequency')
        g.set_titles("{col_name}")

        plt.tight_layout()
        plt.show()


    def view_outliers(self, columns=None, cols=3):
        '''
        Visualises outliers in the specified columns using box plots. If no columns
        are specified, it visualises outliers for all numeric columns.

        Parameters:
        ----------
        columns: list of str, optional
            The list of column names to visualise for outliers. If None, all numeric 
            columns in the DataFrame are visualised.
        cols: int, default=3
            The number of columns in the subplot grid layout.
        '''
        if columns is None:
            columns = self.df.select_dtypes(include='number').columns

        numeric_columns = [col for col in columns if col in self.df.select_dtypes(include='number').columns]

        rows = (len(numeric_columns) + cols -1) // cols
        fig, axes = plt.subplots(rows, cols, figsize=(6 * cols, 5 * rows))
        axes = axes.flatten()

        for i, col in enumerate(numeric_columns):
            sns.boxplot(y=self.df[col], color='lightgreen', ax=axes[i], showfliers=True)

            axes[i].set_title(f'Box plot for {col}')
            axes[i].set_ylabel(col)

        plt.tight_layout()
        plt.show()


    def view_correlation(self):
        '''
        Plots a heatmap to visualize the correlation matrix for all numeric columns in the 
        DataFrame. Cells in the matrix are annotated with correlation values.
        '''
        numeric_df = self.df.select_dtypes(include=np.number)

        corr = numeric_df.corr()

        mask = np.zeros_like(corr, dtype=np.bool_)
        mask[np.triu_indices_from(mask)] = True

        cmap = sns.diverging_palette(220, 10, as_cmap=True)

        sns.heatmap(corr, mask=mask, square=True, linewidths=.5, annot=True,
                    annot_kws={'size': 8}, fmt='.2f', cmap=cmap)
        plt.yticks(rotation=0, fontsize=8)
        plt.xticks(fontsize=8)
        plt.title('Correlation matrix of all Numerical variables')
        plt.show()
