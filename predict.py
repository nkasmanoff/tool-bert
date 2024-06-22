from make_dataset import get_id2tool_name
from train import remove_any_non_alphanumeric_characters
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from tools import tool_labels

model = AutoModelForSequenceClassification.from_pretrained("tool-bert")
tokenizer = AutoTokenizer.from_pretrained("google-bert/bert-base-uncased")

questions = ["Who is the best captain in star trek", "tell me a joke", "get me the news",
                'take a photo', 'check the weather', 'play some music', "take a picture"]
for question in questions:
    question = remove_any_non_alphanumeric_characters(question)
    inputs = tokenizer(question, return_tensors="pt")

    outputs = model(**inputs)

    logits = outputs.logits
    print(question)
    print(logits.argmax().item())
    print(get_id2tool_name(logits.argmax().item(), tool_labels))
    print('-----')
