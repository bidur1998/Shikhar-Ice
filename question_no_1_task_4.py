import spacy
from biobert_embedding.embedding import BiobertEmbedding
from transformers import AutoTokenizer, AutoModel

def extract_entities_spacy(text, model_name):
    nlp = spacy.load(model_name)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_entities_biobert(text):
    biobert = BiobertEmbedding()
    sentences = text.split('.')
    entities = []

    for sentence in sentences:
        embeddings = biobert.sentence_vector(sentence)
        if "disease" in sentence.lower() or "drug" in sentence.lower():
            entities.append(sentence.strip())

    return entities

if __name__ == "__main__":

    input_text_file = 'import spacy
from biobert_embedding.embedding import BiobertEmbedding
from transformers import AutoTokenizer, AutoModel

def extract_entities_spacy(text, model_name):
    nlp = spacy.load(model_name)
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_entities_biobert(text):
    biobert = BiobertEmbedding()
    sentences = text.split('.')
    entities = []

    for sentence in sentences:
        embeddings = biobert.sentence_vector(sentence)
        if "disease" in sentence.lower() or "drug" in sentence.lower():
            entities.append(sentence.strip())

    return entities

if __name__ == "__main__":

    input_text_file = '/content/drive/output_text'
    text = ""

    with open(input_text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract entities using spaCy models
    entities_spacy_en_core_sci_sm = extract_entities_spacy(text, 'en_core_sci_sm')
    entities_spacy_en_ner_bc5cdr_md = extract_entities_spacy(text, 'en_ner_bc5cdr_md')

    # Extract entities using BioBERT
    entities_biobert = extract_entities_biobert(text)

    print("Entities detected by spaCy (en_core_sci_sm):", entities_spacy_en_core_sci_sm)
    print("Entities detected by spaCy (en_ner_bc5cdr_md):", entities_spacy_en_ner_bc5cdr_md)
    print("Entities detected by BioBERT:", entities_biobert)
'
    text = ""

    with open(input_text_file, 'r', encoding='utf-8') as file:
        text = file.read()

    # Extract entities using spaCy models
    entities_spacy_en_core_sci_sm = extract_entities_spacy(text, 'en_core_sci_sm')
    entities_spacy_en_ner_bc5cdr_md = extract_entities_spacy(text, 'en_ner_bc5cdr_md')

    # Extract entities using BioBERT
    entities_biobert = extract_entities_biobert(text)

    print("Entities detected by spaCy (en_core_sci_sm):", entities_spacy_en_core_sci_sm)
    print("Entities detected by spaCy (en_ner_bc5cdr_md):", entities_spacy_en_ner_bc5cdr_md)
    print("Entities detected by BioBERT:", entities_biobert)