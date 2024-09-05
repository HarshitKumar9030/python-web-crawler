import os
import sqlite3
import csv

def save_data(data, output_type, output_path):
    if output_type == 'sqlite':
        save_to_sqlite(data, output_path)
    elif output_type == 'csv':
        save_to_csv(data, output_path)

def save_to_sqlite(data, db_path):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS content (
        id INTEGER PRIMARY KEY,
        text TEXT,
        code_block TEXT,
        important_text TEXT
    )
    ''')

    max_len = max(len(data['text']), len(data['code_blocks']), len(data['important_text']))

    for i in range(max_len):
        text = data['text'][i] if i < len(data['text']) else ""
        code_block = data['code_blocks'][i] if i < len(data['code_blocks']) else ""
        important_text = data['important_text'][i] if i < len(data['important_text']) else ""
        
        cursor.execute('INSERT INTO content (text, code_block, important_text) VALUES (?, ?, ?)',
                       (text, code_block, important_text))

    conn.commit()
    conn.close()

def save_to_csv(data, csv_path):
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    max_len = max(len(data['text']), len(data['code_blocks']), len(data['important_text']))

    with open(csv_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['text', 'code_block', 'important_text'])
        for i in range(max_len):
            text = data['text'][i] if i < len(data['text']) else ""
            code_block = data['code_blocks'][i] if i < len(data['code_blocks']) else ""
            important_text = data['important_text'][i] if i < len(data['important_text']) else ""
            writer.writerow([text, code_block, important_text])
