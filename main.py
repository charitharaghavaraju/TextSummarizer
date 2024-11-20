from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Stage 01: Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"Completed {STAGE_NAME}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME1 = "Stage 02: Data Validation"

try:
    logger.info(f"Starting {STAGE_NAME1}")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f"Completed {STAGE_NAME1}")
except Exception as e:
    logger.exception(e)
    raise e