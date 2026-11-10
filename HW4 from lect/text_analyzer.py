import os
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def read_text_file(file_path):
    """"Читає тект з файлу та перевіряє, чи існує файл та чи він не порожній."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f" Файл {file_path} не знайдено!")

    with open(file_path, 'r', encoding="utf-8") as file:
        text = file.read()

    if not text.strip():
        raise ValueError(f" Файл {file_path} порожній!")
    
    return text

def analyze_text(text):
    """Анаізує текст - підраховує кількість слів, речень та унікальних слів."""
    text = read_text_file(file_path=text)

    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens if word.isalpha()]
    num_words = len(words)

    if num_words == 0:
        raise ValueError("У файлі немає тексту для аналізу!")

    freq_dist = nltk.FreqDist(words)

    freq_table = pd.DataFrame(freq_dist.most_common(), columns=['Слово', 'Частота вживання'])
    freq_table.index = range(1, len(freq_table) + 1)

    return num_words, freq_table

if __name__ == "__main__":
    filename = "text.txt"
    try:
        count, table = analyze_text(filename)
        print(f"Кількість слів у тексті: {count}")
        print("Таблиця частоти вживання слів:") 
        print(table.head(10))
    except Exception as e:
        print(f"Помилка: {e}")