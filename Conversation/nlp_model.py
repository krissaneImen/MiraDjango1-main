import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier

def load_data_from_json(file_path):
    with open("/Users/zitouni/python_stuff/MiraDjango1-main/course_support_data.json", 'r') as file:
        data = json.load(file)
    corpus = [(item['question'], item['answer']) for item in data]
    return corpus

# Charger les données depuis le fichier JSON spécifique au support de cours
corpus = load_data_from_json('course_support_data.json')

def train_model(corpus):
    nltk.download('punkt')
    sentences, responses = zip(*corpus)
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sentences)
    
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(X, responses)
    
    return vectorizer, classifier

vectorizer, classifier = train_model(corpus)

def generate_response(user_input):
    user_input_vector = vectorizer.transform([user_input])
    response = classifier.predict(user_input_vector)[0]
    return response

# Exemple d'utilisation
if __name__ == "__main__":
    user_input = input("Vous: ")
    print("Chatbot:", generate_response(user_input))
