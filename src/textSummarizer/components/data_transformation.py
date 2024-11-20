import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        #tokenizer_name = config.tokenizer_name.replace("\\", "/")
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, examples):
        input_embeddings = self.tokenizer(examples['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_embeddings = self.tokenizer(examples['summary'], max_length=1024, truncation=True)

        return {
            'input_ids': input_embeddings['input_ids'],
            'attention_mask': input_embeddings['attention_mask'],
            'labels': target_embeddings['input_ids']
        }
    
    def convert_data(self):
        samsum_dataset = load_from_disk(self.config.data_path)
        samsum_dataset_pt = samsum_dataset.map(self.convert_examples_to_features, batched=True)
        samsum_dataset_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))