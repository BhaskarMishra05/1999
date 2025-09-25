import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

@dataclass
class DATA_INGESTION_CONFIG:
    raw_data_path: str = os.path.join('artifacts','raw.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    train_data_path: str = os.path.join('artifacts', 'train.csv')

class DATA_INGESTION:
    def __init__(self):
        self.data_ingestion_config_obj = DATA_INGESTION_CONFIG()

    def data_ingestion(self):
        try:
            
            logging.info('Starting Data Ingestion Stage')
            logging.info('loading the file into a variable dataframe "raw_dataframe"')

            raw_dataframe = pd.read_csv(self.data_ingestion_config_obj.raw_data_path, sep=',')

            logging.info('Spliting the raw dataframe into training set and testing set')
            train_set, test_set = train_test_split(raw_dataframe, test_size= 0.3, random_state= 42)

            logging.info('Saving the train and test set files into artifacts folder')

            train_set.to_csv(self.data_ingestion_config_obj.train_data_path, index = False)
            test_set.to_csv(self.data_ingestion_config_obj.test_data_path, index = False)
            
            logging.info('Successfully executed data ingestion stage ')
            return (
                self.data_ingestion_config_obj.test_data_path,
                self.data_ingestion_config_obj.train_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)