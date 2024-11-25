# exploratory-data-analysis---customer-loans-in-finance

## table of contents
1. [Dependencies](#Dependencies)
2. [Description](#Description)
3. [Installation instructions](#Installation-instructions)
4. [Usage](#Usage)
5. [Files](#Files)
6. [Step-by-step guide of project workflow](#Step-by-step-guide-of-project-workflow)
7. [License](#License)

## Dependencies
- `matplotlib`
- `numpy`
- `Python` 
- `Pandas`
- `seaborn`
- `Sqlalchemy`
- `Yaml`


## Description
### Aim of the Project
The aim of this project is to extract a dataset(`loan_payments`) from an AWS RDS instance and perform exploratory data analysis (EDA). This analysis aims to:
- Understand the dataset through transformations, visualizations, and insights.

Another aim of the project was to analyse specific columns in the dataset and assess whether certain criteria causes an increase in risk that a customer would not be able to repay their loan back in full. This would be supported by visualisations of the dataset to see the results found.

### Results Found
From the first part of this project, the EDA, I examined the dataset and transformed the data so I could interpret thew skew, outliers and correlation playing a part ...

For the second part of this project, I was able to analyse specific columns within the dataset to establish specific values for the company in regards to their revenue loss and number of loans that have become Charged Off or are at risk of becoming Charged Off. I was able to determine that a customers loan Grade and Purpose for having a loan affected the risk to whether a loan would be paid back in full or not. A lower loan Grade (Grades D, E or F) resulted in a loan being more of a risk for the company and that a customers purpose of having a loan for a small business would be a significant increase in risk that a loan would not be paid back in full. With these insights the company would now be able to re-strategise the loans they give to customers based on certain criteria to prevent revenue loss for the company.

### Visualisations of data
- **Correlation Matrix:**
  A heatmap visualising correlations between transformed columns in the dataset.

![image](https://github.com/user-attachments/assets/93655245-9eff-4d2d-92e8-6e3979d23d93)

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
   '''bash
   git clone https://github.com/SteenMaxwell/exploratory-data-analysis---customer-loans-in-finance681.git
   '''

2) Install dependencies:
   '''bash
   pip install (create a txt file for dependencies)
   '''

## Usage
1) **Run EDA workflow:**
   Open the `EDA_final_workflow.ipynb` notebook to perform exploratory data analysis and generate key insights.

2) **Run analysis overview:**
   Open the analysis.ipynb notebook to analyze risk factors and generate advanced visualisations.

## Files
`db_utils.py` - Contains python code to extract and save the data to a csv file from an AWS RDS database. The code in this file initialises a SQLAlchemy engine to do this, and stores the data locally in a pandas DataFrame.

`loan_payments_data.csv` - Database containing all the columns and rows needed for an EDA analysis


## Step-by-step guide of project workflow


## License 
This project is licensed under ...
