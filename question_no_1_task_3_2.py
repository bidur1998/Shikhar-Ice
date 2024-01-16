from transformers import AutoTokenizer
from collections import Counter
import string

def count_unique_tokens(file_path, model_name_or_path):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text, add_special_tokens=True)))

    token_counts = Counter(tokens)

    top30_tokens = token_counts.most_common(30)

    return top30_tokens

if __name__ == "__main__":

    input_text_file = 'from transformers import AutoTokenizer
from collections import Counter
import string

def count_unique_tokens(file_path, model_name_or_path):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text, add_special_tokens=True)))

    token_counts = Counter(tokens)

    top30_tokens = token_counts.most_common(30)

    return top30_tokens

if __name__ == "__main__":

    input_text_file = '/content/drive/output_text'
    model_name_or_path = 'bert-base-uncased'

    top30_tokens = count_unique_tokens(input_text_file, model_name_or_path)

    print(f'Top 30 tokens and their counts:')
    for token, count in top30_tokens:
        print(f'{token}: {count}')
'
    model_name_or_path = 'bert-base-uncased'

    top30_tokens = count_unique_tokens(input_text_file, model_name_or_path)

    print(f'Top 30 tokens and their counts:')
    for token, count in top30_tokens:
        print(f'{token}: {count}')