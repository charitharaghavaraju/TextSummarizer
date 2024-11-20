from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger
from textSummarizer.components.model_trainer import ModelTrainer


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()