import spacy
import textacy.extract

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# The text we want to examine
text = ""
# Parse the document with spaCy
doc = nlp(text)

# Extract semi-structured statements
statements = textacy.extract.semistructured_statements(doc, "moscow")

# Print the results
print("Here are the things I know:")

for statement in statements:
    subject, verb, fact = statement
    print(f" - {subject, verb, fact} ")
