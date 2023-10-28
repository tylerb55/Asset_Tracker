# run from here https://colab.research.google.com/drive/19xhoVy_YJVoG_Xe7EhRJkwLdAsDlVxfG#scrollTo=sF84BnI2Jyao
from transformers import XLNetTokenizer, XLNetForSequenceClassification, Trainer, TrainingArguments
import numpy as np
from datasets import load_dataset


tokenizer = XLNetTokenizer.from_pretrained("xlnet-base-cased")

#train_dataset = load_dataset("csv", data_files={"train": "train.csv"})
#test_dataset = load_dataset("csv", data_files={"test": "test.csv"})

#train_encodings = tokenizer(train_dataset['sentence'], truncation=True, padding=True)

train_dataset = load_dataset("financial_phrasebank", "sentences_50_agree", split="train")
test_dataset = load_dataset("financial_phrasebank", "sentences_allagree", split="train")

def tokenize_function(examples):
    return tokenizer(train_dataset['sentence'], truncation=True, padding='Max_length', max_length=128)

tokenized_train = train_dataset.map(tokenize_function, batched=True)

model = XLNetForSequenceClassification.from_pretrained("xlnet-base-cased", num_labels=3)

training_args = TrainingArguments(
    output_dir='./results',          # output directory
    num_train_epochs=5,              # total number of training epochs
    per_device_train_batch_size=16,  # batch size per device during training
    per_device_eval_batch_size=64,   # batch size for evaluation
    warmup_steps=250,
    weight_decay=0.01,
    logging_dir='./logs',            # directory for storing logs
    logging_steps=10,
)

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return {"accuracy": (predictions == labels).astype(np.float32).mean().item()}

trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = tokenized_train,
    compute_metrics = compute_metrics
)

trainer.train()

trainer.evaluate(test_dataset)

trainer.save_model("fine-tuned-model")



