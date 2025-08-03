from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        trainingpipelinconfig=TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelinconfig)
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("initiate the data ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("data ingestion completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelinconfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("initiate data validation")
        datavalidationartifact=data_validation.initiate_data_validation()
        logging.info("data validation completed")
        print(datavalidationartifact)
        

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
