# final project
import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Ensure that the necessary NLTK resources are downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def main():
    # File path to be analyzed
    file_path = "words.txt"
    
    # Load text from file
    text = read_text_from_file(file_path)
    
    # Tokenize text into words
    words = tokenize_text(text)
    
    # Lemmatize words
    lemmatized_words = lemmatize_words(words)
    
    # Get stop words from nltk and add custom stop words
    stop_words = set(stopwords.words('english'))
    custom_stop_words = {'osu', 'next', '1', 'fit'}
    stop_words.update(custom_stop_words)
    
    # Filter out the stop words
    filtered_words = [word for word in lemmatized_words if word not in stop_words]

    # Count word frequencies using Counter
    frequency_dict = Counter(filtered_words)
    
    # Get the top 10 most common words
    top_10_words = frequency_dict.most_common(10)
    
    # Print the top 10 words with their frequencies
    for word, count in top_10_words:
        print_histogram_bar(word, count)
    
    # Visualize the word cloud
    visualize_wordcloud(frequency_dict)

def print_histogram_bar(word, count):
    print(f"{word:<15} : {'X' * count}")

def read_text_from_file(file_path):
    # Reads text from a file
    with open(file_path, 'r', encoding="utf-8") as file_reader:
        text = file_reader.read()
    return text

def tokenize_text(text):
    """Tokenizes text into words."""
    words = re.findall(r'\w+', text.lower())
    return words

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)

def lemmatize_words(words):
    """Lemmatizes a list of words with POS tagging."""
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in words]
    return lemmatized_words

def visualize_wordcloud(word_counts):
    """Visualizes word counts using a word cloud."""
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_counts)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

if __name__ == "__main__":
    main()
