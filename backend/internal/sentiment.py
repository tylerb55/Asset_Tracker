from transformers import pipeline, XLNetTokenizer, XLNetForSequenceClassification
from models import Sentiment

model = XLNetForSequenceClassification.from_pretrained("fine-tuned-model")
tokenizer = XLNetTokenizer.from_pretrained("fine-tuned-model")
sentiment_analysis = pipeline("sentiment_analysis", model=model, tokenizer=tokenizer)

with open("data.txt") as f:
    lines = f.read()

results = sentiment_analysis(lines)

for result in results:
    sentence = result['sentence']
    sentiment_label = result['label']
    score = result['score']
    print(f"{sentence} {sentiment_label} {score}")
    sentiment = Sentiment(sentence=sentence,label=sentiment_label,score=score)