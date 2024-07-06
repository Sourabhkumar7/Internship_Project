import os
import pandas as pd
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
import re

nltk.download('punkt')
nltk.download('stopwords')

input_df = pd.read_excel('input.xlsx')

stop_words = set(stopwords.words('english'))

def count_syllables(word):
    vowels = 'aeiou'
    word = word.lower()
    count = sum(1 for letter in word if letter in vowels)
    if word.endswith('e'):
        count -= 1
    return count if count > 0 else 1


def analyze_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    sentences = nltk.sent_tokenize(text)
    
    words = nltk.word_tokenize(text)

    word_count = len(words)
    
    with open('positive-words.txt', 'r') as file:
        positive_words = file.read().split()
    
    with open('negative-words.txt', 'r') as file:
        negative_words = file.read().split()
    
    positive_words = set(positive_words)
    negative_words = set(negative_words)
    
    positive_score = 0
    negative_score = 0

    for word in words:
        word_lower = word.lower()
        if word_lower in positive_words:
            positive_score += 1
        elif word_lower in negative_words:
            negative_score += 1
    
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
 
    avg_sentence_length = sum(len(nltk.word_tokenize(sentence)) for sentence in sentences) / len(sentences)
    complex_word_count = sum(1 for word in words if count_syllables(word) > 2)
    percentage_complex_words = complex_word_count / word_count
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    avg_words_per_sentence = word_count / len(sentences)
    syllables_per_word = sum(count_syllables(word) for word in words) / word_count
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    avg_word_length = sum(len(word) for word in words) / word_count
    
    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Avg Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_complex_words,
        'Fog Index': fog_index,
        'Avg Number of Words Per Sentence': avg_words_per_sentence,
        'Complex Word Count': complex_word_count,
        'Word Count': word_count,
        'Syllable per Word': syllables_per_word,
        'Personal Pronouns': personal_pronouns,
        'Avg Word Length': avg_word_length
    }

results = []
for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    with open(f'articles/{url_id}.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    analysis_result = analyze_text(text)
    results.append({**row, **analysis_result})

output_df = pd.DataFrame(results)
output_df.to_excel('output.xlsx', index=False)

print("Data analysis completed!")
