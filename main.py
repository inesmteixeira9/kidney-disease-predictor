from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME_01

try:
    logger.info(f">>>>>> stage {STAGE_NAME_01} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e