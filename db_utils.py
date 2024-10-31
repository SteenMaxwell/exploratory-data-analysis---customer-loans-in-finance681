import yaml
import pandas as pd
import sqlalchemy

def loading_credentials():
    with open('credentials.yaml', 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials.get('RDS_HOST')
        self.user = credentials.get('RDS_USER')
        self.password = credentials.get('RDS_PASSWORD')
        self.database = credentials.get('RDS_DATABASE')
        self.port = credentials.get('RDS_PORT')

    
    def initialise_engine(self):
        connection = (f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}')
        self.engine = sqlalchemy.create_engine(connection)


    def extract_data(self):
        loan_payments_df = pd.read_sql_table('loan_payments', self.engine)
        return loan_payments_df
    
    def save_data_csv(self, loan_payments_df):
        loan_payments_df.to_csv('loan_payments_data.csv', index=False)

credentials = loading_credentials()
connector = RDSDatabaseConnector(credentials)
connector.initialise_engine()
loan_payments_df = connector.extract_data()
connector.save_data_csv(loan_payments_df)
print(loan_payments_df.head())



def loading_data():
    loan_payments_df = pd.read_csv('loan_payments_data.csv')
    return loan_payments_df


