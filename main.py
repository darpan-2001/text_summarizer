from src.text_summarizer.logging import logger
from text_summarizer.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="DATA INGESTION STAGE"

try:
    logger.info(f"{STAGE_NAME} started............")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STAGE_NAME} completed.")
except Exception as e:
    logger.exception(e)
    raise e

# logger.info("this is s custom log")