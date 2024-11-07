from yaml import safe_load
import pandas as pd
from sqlalchemy import create_engine


def loading_credentials():
    '''
    This function loads the credentials from a YAML file for the AWS RDS so the dataset can be accessed locally.

    Returns:
    -------
    returns the credentials given in the credentials.yaml file.
    '''
    
    with open('credentials.yaml', 'r') as file:
        credentials = safe_load(file)
    return credentials


class RDSDatabaseConnector:
    '''
    Used to ultimately access an AWS RDS database and save the 'loan_payments' table to a CSV file so it can be accessed locally.

    Methods:
    -------
    initialise_engine()
        initialises a SQLAchemy engine. 

    extract_data()
        extracts 'loan_payments' from RDS database.

    save_data_csv(loan_payments_df)
        saves pandas DataFrame to a CSV file.

    '''


    def __init__(self, credentials):
        '''
        initialises RDSDatabaseConnector with the database credentials.

        Parameters:
        ----------
        credentials: dict
            a dictionary of credentials that loading_credentials function will extract. 

        Attributes:
        ----------   
        RDS_HOST: Database host URL
        RDS_USER: Database username
        RDS_PASSWORD: Database password
        RDS_DATABASE: Database name
        RDS_PORT: Database port
        '''

        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')

    
    def initialise_engine(self):
        '''
        This method initialises a SQLAlchemy engine using the credentials given. 
        '''

        connection = (f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
        self.engine = create_engine(connection)


    def extract_data(self):
        '''
        This method extracts the dataset 'loan_payments' from the AWS RDS database and returns it as a pandas DataFrame.

        Returns:
        -------
        returns a pandas DataFrame of the 'loan_payments' table from the RDS database.
        '''

        loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
        return loan_payments_df


def save_data_csv(df):
    '''
    This method saves the DataFrame to a CSV file.

    Parameters:
    ----------
    loan_payments_df: DataFrame
        pandas DataFrame of 'loan_payments' from the RDS database.
    '''

    df.to_csv('loan_payments_data.csv', index=False)


def loading_data():
    '''
    This function loads the data from the CSV file to a pandas DataFrame and returns it.

    Returns:
    -------
    returns pandas DataFrame of 'loan_payments'.
    '''

    df = pd.read_csv('loan_payments_data.csv')
    return df


credentials_needed = loading_credentials()
connector = RDSDatabaseConnector(credentials_needed)
connector.initialise_engine()
loan_payments_df = connector.extract_data()
save_data_csv(loan_payments_df)