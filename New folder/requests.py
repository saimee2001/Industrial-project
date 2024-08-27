import requests
from bs4 import BeautifulSoup 
import torch
import torch.nn as nn
import re
import torch
from transformers import BertTokenizer, BertModel
print(torch.cuda.is_available()) 

# Step 1: Scrape the text data from the website
url = 'https://www.dhakatribune.com/bangladesh'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all the text from paragraphs on the webpage
text_data = ' '.join([p.text for p in soup.find_all('p')])

print(text_data[:500])  # Print the first 500 characters



# Step 2: Preprocess the text data
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

cleaned_text = preprocess_text(text_data)
print(cleaned_text[:500])  # Print the first 500 characters of the cleaned text


# ... (rest of your code)

# Get BERT embeddings
with torch.no_grad():
    outputs = model(**tokens)
from transformers import BertTokenizer, BertModel

# Step 3: Load pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize the text
tokens = tokenizer(cleaned_text, return_tensors='pt', truncation=True, padding=True, max_length=512)

# Get BERT embeddings
with torch.no_grad():
    outputs = model(**tokens)

embeddings = outputs.last_hidden_state
print(embeddings.shape)  # Print the shape of the embeddings


# Define a simple classification model
class SimpleBERTClassifier(nn.Module):
    def __init__(self, bert_model):
        super(SimpleBERTClassifier, self).__init__()
        self.bert = bert_model
        self.classifier = nn.Linear(bert_model.config.hidden_size, 2)  # Binary classification example
    
    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask=attention_mask)
        cls_output = outputs.last_hidden_state[:, 0, :]  # CLS token output
        logits = self.classifier(cls_output)
        return logits

# Instantiate the model
model = SimpleBERTClassifier(model)

# Example of getting logits (for training, you'll need labels and loss computation)
logits = model(tokens['input_ids'], tokens['attention_mask'])
print(logits)