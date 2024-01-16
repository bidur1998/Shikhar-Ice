import csv
from collections import Counter
import string

def process_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator).lower()

    words = text.split()

    # Count occurrences of each word
    word_counts = Counter(words)

    # Get the top 30 most common words
    top30_words = word_counts.most_common(30)

    return top30_words

def save_to_csv(top30_words, csv_file_path):
    # Save the top 30 words and counts to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Word', 'Count'])  # Header row

        for word, count in top30_words:
            csv_writer.writerow([word, count])

if __name__ == "__main__":

    input_text_file = '/content/drive/output_text'
    output_csv_file = 'top30_words.csv'

    top30_words = process_text(input_text_file)
    save_to_csv(top30_words, output_csv_file)

    print(f'Top 30 words and their counts saved to {output_csv_file}')

from google.colab import drive
drive.mount('/content/drive')