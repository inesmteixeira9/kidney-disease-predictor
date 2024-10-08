from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import (DataIngestionTrainingPipeline, STAGE_NAME_01)
from cnnClassifier.pipeline.stage_02_prepare_base_model import (PrepareBaseModelTrainingPipeline, STAGE_NAME_02)
from cnnClassifier.pipeline.stage_03_model_training import (ModelTrainingPipeline, STAGE_NAME_03)


## Data ingestion
try:
    logger.info(f">>>>>> stage {STAGE_NAME_01} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME_01} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


## Prepare base model
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME_02} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME_02} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


## Model training
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME_03} started <<<<<<")
   model_training = ModelTrainingPipeline()
   model_training.main()
   logger.info(f">>>>>> stage {STAGE_NAME_03} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

