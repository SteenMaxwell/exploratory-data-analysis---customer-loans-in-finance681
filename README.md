# exploratory-data-analysis---customer-loans-in-finance

## table of contents
1. [Dependencies](#Dependencies)
2. [Description](#Description)
3. [Installation instructions](#Installation-instructions)
4. [Usage](#Usage)
5. [Files](#Files)
6. [License](#License)

## Dependencies
- `matplotlib`
- `numpy`
- `Python` 
- `Pandas`
- `scipy.stats`
- `seaborn`
- `Sqlalchemy`
- `Yaml`


## Description
### Aim of the Project
The aim of this project is to extract a dataset(`loan_payments`) from an AWS RDS instance and perform exploratory data analysis (EDA). This analysis aims to:
- Understand the dataset through transformations, visualisations, and insights.

Another aim of the project was to analyse specific columns in the dataset and assess whether certain criteria causes an increase in risk that a customer would not be able to repay their loan back in full. This would be supported by visualisations of the dataset to see the results found.

### Results Found
1) EDA insights:
   - The dataset was cleaned and analysed to address skewness, outliers, and collinearity between columns.
  
2) Analysis of Revenue loss and loss Indicators:
   - The Total Revenue Loss for the company for all Charged Off loans: £67,420,215.03
   - Loan Grade: Customers with lower grades (e.g., Grades D, E, F) posed a significantly higher risk of being Charged Off.
   - Loan Purpose: Loans for purposes like "small business" were highly correlated with increased risk.
  
These findings allow the company to identify high-risk loans and adjust strategies to minimise revenue loss.

### Visualisations of data
- **Correlation Matrix:**
  A heatmap visualising correlations between transformed columns in the dataset.

![image](https://github.com/user-attachments/assets/1ca6d7d2-8c12-4d30-8f66-7c8ade02b623)

- **Revenue Loss Analysis:**
  A pie chart displaying the percentage of lost or at-risk revenue compared to expected revenue.
  
![image](https://github.com/user-attachments/assets/8f328f76-f84e-4c95-8d98-08623caf1942)

- **Loan Grade Risk:**
  A bar plot illustrating the percentage distribution of loan grades for Charged Off, At Risk, and All customers.
  
![image](https://github.com/user-attachments/assets/f7e752d2-b5b1-4cb9-952b-ab485df09823)



### What I learnt throughout the project
- Advanced `pandas` techniques for data manipulation and transformation.
- Effective visualisation skills using `matplotlib` and `seaborn`.
- Enhanced ability to interpret data insights and communicate findings in a structured manner.

## Installation instructions
1) Clone the repository:
   ```bash
   git clone https://github.com/SteenMaxwell/exploratory-data-analysis---customer-loans-in-finance681.git
   ```

2) Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1) **Run EDA workflow:**
   Open the `EDA_final_workflow.ipynb` notebook to perform exploratory data analysis and generate key insights.

2) **Run analysis overview:**
   Open the `analysis.ipynb` notebook to analyze risk factors and generate advanced visualisations.

## Files
`db_utils.py` - Contains python code to extract and save the data to a csv file from an AWS RDS database. The code in this file initialises a SQLAlchemy engine to do this, and stores the data locally in a pandas DataFrame.

`loan_payments_data.csv` - Database containing all the columns and rows needed for an EDA analysis

`EDA_final_workflow.ipynb` - Jupyter notebook that contains the final workflow for performing EDA. This notebook loads the raw dataset, processes the data, handles missing values, explores correlations, and creates various visualisations to summarise the dataset.

`transformed_financial_loan_data.csv` - A CSV file that contains the transformed version of the original financial loan data. This file has undergone data transformations in preparation for analysis.

`analysis.ipynb` - Jupyter notebook that focuses on analyzing the loan data in-depth. Looks at the company's revenue and various factors for revenue loss.

`data_transform.py` - A Python script containing the main class for methods that transform the loan data columns to the correct dtypes.

`data_frame_info.py` - A Python script that contains the main class for methods that extract and summarise information from pandas DataFrames. It is useful for quickly analysing the structure, data types, and summary statistics of datasets.

`data_frame_transform.py` - Contains the main class for applying various data transformations to the DataFrame.

`plotter.py` -   Contains the main class for visualisation methods for plotting various types of graphs. It includes methods for plotting correlation matrices, distribution plots, and boxplots to assist in analysing the data visually.


## License 
This project is licensed under ...
