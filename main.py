from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
from networksecurity.components.data_transformation import DataTransformation,DataTransformationConfig
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainingConfig
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
        logging.info("data transformation started")
        data_transformation_config=DataTransformationConfig(trainingpipelinconfig)
        data_transformation=DataTransformation(datavalidationartifact,data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        logging.info("data transformation completed")
        print(data_transformation_artifact)

        logging.info("model training started")
        model_trainer_config = ModelTrainingConfig(trainingpipelinconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("model training artifact created")

        

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
