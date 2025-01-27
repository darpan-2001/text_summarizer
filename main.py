from src.text_summarizer.logging import logger
from text_summarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline
from text_summarizer.pipeline.data_validation import DataValidationTrainingPipeline
from text_summarizer.pipeline.data_transformation import DataTransformationTrainingPipeline
from text_summarizer.pipeline.model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME="DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} started............")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f"{STAGE_NAME} started............")
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f"{STAGE_NAME} started............")
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"{STAGE_NAME} started............")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
        logger.exception(e)
        raise e


# logger.info("this is s custom log")