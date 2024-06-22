from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
import pandas as pd
from datasets import load_dataset 
import numpy as np
import evaluate
from transformers import TrainingArguments, Trainer
from tools import tool_names

import huggingface_hub

def remove_any_non_alphanumeric_characters(text):
    return ''.join(e for e in text if e.isalnum() or e.isspace())

def compute_metrics(eval_pred, metric=evaluate.load("accuracy")):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=labels)


def main():
    huggingface_hub.login()
    dataset = load_dataset("json", data_files="generated_questions/dataset.json")


    model = AutoModelForSequenceClassification.from_pretrained("google-bert/bert-base-uncased", num_labels=len(tool_names)) 


    tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")

    def tokenize_function(examples):

        return tokenizer(examples["command"], padding="max_length", truncation=True)


    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    train_dataset = tokenized_datasets["train"].shuffle(seed=42)

    training_args = TrainingArguments(output_dir="tool-bert", eval_strategy="epoch", num_train_epochs=4
                                    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=train_dataset,
        compute_metrics=compute_metrics,
    )

    trainer.train()


    # push model to hub 
    trainer.push_to_hub("tool-bert")


if __name__ == "__main__":
    main()