# 🧹 Text Preprocessing with NLTK

This project provides a complete and customizable **text preprocessing pipeline** using [NLTK (Natural Language Toolkit)](https://www.nltk.org/). The pipeline includes common steps required before feeding text data into NLP or Machine Learning models.

---

## 🧠 What It Does

The `preprocessing_text` function performs the following steps on English text:

1. **Lowercasing** – Converts all characters to lowercase.
2. **Punctuation Removal** – Removes all punctuation except apostrophes.
3. **Whitespace Normalization** – Removes extra spaces.
4. **Tokenization** – Splits the text into individual words using NLTK's `word_tokenize`.
5. **Stopword Removal** – Removes common English stopwords.
6. **POS Tagging** – Tags words with their Part-of-Speech.
7. **Lemmatization** – Lemmatizes each word based on its POS tag using WordNet.

---

## 🔧 Requirements

- Python 3.6+
- `nltk`

Install required packages:

```bash
pip install nltk
````

Download NLTK resources (included in the script, runs only once):

```python
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
```

---

## 🚀 How to Use

### ✅ Sample Usage

```python
from your_script import preprocessing_text

text = "Dogs are running in the park! It's a beautiful day, isn't it?"
tokens = preprocessing_text(text)
print(tokens)
```

### 🔍 Sample Output

```
['dog', 'run', 'park', 'beautiful', 'day']
```

---

## 🧩 Function Signature

```python
def preprocessing_text(text: str) -> List[str]
```

Returns a list of preprocessed, lemmatized tokens from the input sentence.

---

## 📁 File Structure

```
├── text_preprocessing.py
├── README.md
```

---

> This module can be easily integrated into larger NLP pipelines, sentiment analysis systems, or classification models.


- فایل `requirements.txt` بسازم  
- نسخه فارسی این README رو هم آماده کنم  
- یا این ماژول رو با `Streamlit` یا `Flask` به یک API تبدیل کنیم (برای پروژه واقعی)

بگو تا باهات جلو بریم.
```
