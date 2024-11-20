from transformers import Trainer, TrainingArguments
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
import os

from textSummarizer.entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # Load the dataset
        samsum_data_pt = load_from_disk(self.config.data_path)

        # Define the training arguments
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_dir=self.config.root_dir,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps,
            report_to="none"
        )

        trainer = Trainer(
            model=model_pegasus, processing_class=tokenizer,
            data_collator=seq2seq_data_collator,
            args=training_args,
            train_dataset=samsum_data_pt['test'],    # Use the test dataset for training as the dataset is small and easy to train. Change to 'train' for larger datasets.
            eval_dataset=samsum_data_pt['validation']
        )

        # Train the model
        trainer.train()

        # Save the model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_model"))

        # Save the tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_tokenizer"))