from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
import wikipedia

# Specify the title of the Wikipedia page
wiki = wikipedia.page('Sam_Altman')
# Extract the plain text content of the page
text = wiki.content
print(text)

model_name = "deepset/roberta-base-squad2"

# Load the model and tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create question-answering pipeline
nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)

# context = ""

while True:
    user_input = input("Ask a question or press 'q' to quit: ")

    if user_input.lower() == 'q':
        break

    QA_input = {
        'question': user_input,
        'context': text
    }

    model_response = nlp(QA_input)

    print(f"Complete response: {model_response}")
    print(f"Answer: {model_response['answer']}")