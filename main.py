# CONTRACT INFORMATION EXTRACTION USING NER + REGEX (FINAL VERSION)

import spacy
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Sample contract text
text = """
This Agreement is made on 12 March 2023 between John Doe and ABC Pvt Ltd.
The total payment of $5000 shall be made within 6 months.
The contract will remain valid for 2 years from the start date.
"""

# Apply NLP
doc = nlp(text)

# Lists
names = []
organizations = []
dates = []

# Extract entities
for ent in doc.ents:
    if ent.label_ == "PERSON":
        names.append(ent.text)

    elif ent.label_ == "ORG":
        organizations.append(ent.text)

    elif ent.label_ == "DATE":
        if any(char.isdigit() for char in ent.text):
            dates.append(ent.text)

# Regex extraction
amounts = re.findall(r'[\$₹]\s?\d+', text)
durations = re.findall(r'\b\d+\s(?:months?|years?)\b', text)

# Remove duplicates + sort
names = sorted(set(names))
organizations = sorted(set(organizations))
dates = sorted(set(dates))
amounts = sorted(set(amounts))
durations = sorted(set(durations))

# Output
print("\n========== CONTRACT ANALYSIS RESULT ==========")

print("\n👤 Names:")
for n in names:
    print("•", n)

print("\n🏢 Organizations:")
for org in organizations:
    print("•", org)

print("\n📅 Dates:")
for d in dates:
    print("•", d)

print("\n💰 Amounts:")
for a in amounts:
    print("•", a)

print("\n⏳ Durations:")
for dur in durations:
    print("•", dur)

print("\n=============================================")