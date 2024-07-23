# Importer la bibliothèque spaCy
import spacy
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Charger le modèle de langue française
nlp = spacy.load("fr_core_news_sm")

# Fonction pour répondre aux messages en utilisant le traitement du langage naturel (NLP)
def respond_to_message_nlp(message):
    # Traiter le message en utilisant spaCy
    doc = nlp(message)
    print(doc)
    
    # Exemple : Extraire les entités nommées du message
    entities = [ent.text for ent in doc.ents]
    
    # Exemple : Déterminer l'intention du message
    intent = determine_intent(doc)
    
    # Générer une réponse basée sur l'analyse
    response = generate_response(intent, entities)
    
    return response

# Fonction d'exemple pour déterminer l'intention du message
def determine_intent(doc):
    # Ceci est un espace réservé, vous implémenteriez votre propre logique ici
    # Par exemple, vous pourriez analyser les verbes et les noms pour déterminer l'intention
    return "salutation"  # Valeur de l'espace réservé

# Fonction d'exemple pour générer une réponse basée sur l'intention et les entités
def generate_response(intent, entities):
    # Ceci est un espace réservé, vous implémenteriez votre propre logique ici
    # En fonction de l'intention et des entités, générer une réponse appropriée
    if intent == "salutation":
        return "Bonjour ! Comment puis-je vous aider aujourd'hui ?"
    else:
        return "Je suis désolé, je ne sais pas comment répondre à cela."

# Tester la fonction
message = "Pouvez-vous m'aider à trouver un restaurant à proximité ?"
response = respond_to_message_nlp(message)
print(response)

from django.http import JsonResponse
""" 
@api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = respond_to_message_nlp(message)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})


 """

from django.shortcuts import render
from ..Conversation.nlp_model import generate_response

def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        bot_response = generate_response(user_input)
        
        
        return JsonResponse({'response': bot_response})
    return render({'response': bot_response})
