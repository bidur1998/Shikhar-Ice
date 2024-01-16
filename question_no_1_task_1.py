import pandas as pd
import os

# Specify the path to the uploaded folder
uploaded_folder_path = 'C:/Users/Bidur Chautariya/OneDrive/Desktop/Assignments/CVS File'

# List all CSV files in the uploaded folder
csv_files = [file for file in os.listdir(uploaded_folder_path) if file.endswith('.csv')]

# Loop through each CSV file and extract text
for csv_file in csv_files:
    # Read the CSV file using pandas
    df = pd.read_csv(os.path.join(uploaded_folder_path, csv_file))

    # Print column names for each CSV file
    print(f"Columns in {csv_file}: {df.columns.tolist()}")

    # Assuming the column containing large text is named 'text', you can replace it with your actual column name
    text_column = 'text'

    # Check if the specified text column exists in the DataFrame
    if text_column in df.columns:
        # Extract text from the specified column
        texts = df[text_column].tolist()
        # Append the texts to the list
        all_texts.extend(texts)

# Write the extracted texts into a single text file
output_text_file = 'output_text.txt'
with open(output_text_file, 'w', encoding='utf-8') as output_file:
    for text in all_texts:
        output_file.write(str(text) + '\n')

print(f"Texts extracted from {len(csv_files)} CSV files and stored in {output_text_file}")