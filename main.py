from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline
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


STAGE_NAME2 = "Stage 03: Data Transformation"

try:
    logger.info(f"Starting {STAGE_NAME2}")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f"Completed {STAGE_NAME2}")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME3 = "Stage 04: Model Training"

try:
    logger.info(f"Starting {STAGE_NAME3}")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f"Completed {STAGE_NAME2}")
except Exception as e:
    logger.exception(e)
    raise e