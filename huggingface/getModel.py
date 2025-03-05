from transformers import AutoModelForSequenceClassification, AutoTokenizer

# Load the model and tokenizer from Hugging Face
model_name = "Falconsai/text_summarization"  # Replace with any model name
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Save the model and tokenizer locally
model.save_pretrained("/home/larry/local_text_summarizastion")
tokenizer.save_pretrained("/home/larry/local_text_summarizastion")