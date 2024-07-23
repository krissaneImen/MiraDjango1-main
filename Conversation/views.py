from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Conversation
from .Serializers import ConversationSerializer



""" @api_view(['POST'])
def create_conversation(request):
    if request.method == 'POST':
        conversation_serializer = ConversationSerializer(data=request.data)
        if conversation_serializer.is_valid():
            conversation_serializer.save()
            return Response(conversation_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(conversation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

 """
from django.http import JsonResponse
from .models import Conversation, Message
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation
import json
from datetime import datetime

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Conversation
from datetime import datetime

@csrf_exempt
@api_view(['POST'])
def create_conversation(request, cin):
    if request.method == 'POST':
        # Créer une nouvelle conversation
        titre = f"Conversation avec l'utilisateur {cin}"
        date_conversation = datetime.now().date()
        conversation = Conversation(
            Titre=titre,
            CinUser=cin,
            dateConversation=date_conversation,
            Messages=[]
        )
        conversation.save()
        
        # Récupérer l'ID de la conversation
        conversation_id = str(conversation.id)
        
        # Retourner la réponse avec l'ID de la conversation
        response_data = {
            'id': conversation_id,
            **conversation.to_dict()
        }
        
        return JsonResponse(response_data, safe=False)
    return JsonResponse({'error': 'Méthode de requête invalide'}, status=400)



@csrf_exempt
def get_conversation(request, idConversation):
    if request.method == 'GET':
        # Récupérer la conversation existante
        conversation = Conversation.objects(id=idConversation)
        if conversation:
            return JsonResponse(conversation.to_dict(), safe=False)
        else:
            return JsonResponse({'error': 'Aucune conversation trouvée pour cet utilisateur'}, status=404)
    return JsonResponse({'error': 'Méthode de requête invalide'}, status=400)



@csrf_exempt
@api_view(['POST'])
def add_message(request, conversation_id):
    if request.method == 'POST':
        conversation = Conversation.objects(id=conversation_id).first()
        if not conversation:
            return JsonResponse({'error': 'Conversation not found'}, status=404)

        data = json.loads(request.body)
        user = data.get('user')
        contenu = data.get('Contenu')
        date = data.get('date', datetime.now().date())
        heure = data.get('heure', datetime.now().strftime('%H:%M:%S'))

        message = conversation.create_message(
            user=user,
            Contenu=contenu,
            date=date,
            heure=heure
        )
        return JsonResponse(message.to_dict(), safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)



@api_view(['PUT'])
def update_conversation(request, idConversation):
    try:
        conversation = Conversation.objects.get(id=idConversation)
    except Conversation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    conversation_data = request.data
    serializer = ConversationSerializer(conversation, data=conversation_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_conversation_by_id(request, idConversation):
    if request.method == 'GET':
        try:
            conversation = Conversation.objects.get(id=idConversation)
        except Conversation.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_Message_by_conversation(request, idConversation):
    if request.method == 'GET':
        try:
            # Récupérer le groupe spécifié par l'identifiant
            conversation = Conversation.objects.get(id=idConversation)
        except Conversation.DoesNotExist:
            return Response({"conversation": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        # Liste des étudiants du groupe
        messages_list = []

        # Parcourir chaque étudiant dans le groupe
        for message in conversation.Messages:
            message_data = {
                'user': message.user,
                'Contenu': message.Contenu,
                'timestamp': str(message.date) + ' ' + str(message.heure),
                'date': message.date,
                'heure': message.heure,
                # Ajoutez d'autres champs d'étudiant que vous voulez inclure
            }
            messages_list.append(message_data)

        return Response(messages_list, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def get_all_conversation(request, cin):
    if request.method == 'GET':
        conversations = Conversation.objects.filter(CinUser=cin)
        serialized_conversations = []
        for conversation in conversations:
            conversation_data = conversation.to_dict()
            conversation_data['Messages'] = [message.to_dict() for message in conversation.Messages]
            serialized_conversations.append(conversation_data)
        return Response(serialized_conversations, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['DELETE'])
def delete_Conversation(request, idConversation):
    try:
        # Recherchez le groupe par son identifiant
        groupe = Conversation.objects.get(id=idConversation)
    except Conversation.DoesNotExist:
        return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

    # Suppression du groupe
    groupe.delete()
    return Response({"message": "Groupe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Conversation_list(request):
    
    """
    Récupère la liste des enseignants avec leur nom, prénom et CIN.

    Retour :
    - Response : réponse HTTP avec la liste des enseignants et leurs détails.
    """
    if request.method == 'GET':
        conversations = Conversation.objects.all()
        data = [{'conversationTitre': conversation.Titre ,'id' : str(conversation.id)} for conversation in conversations]
        return Response(data, status=status.HTTP_200_OK)



""" 
# Importer la bibliothèque spaCy
import spacy

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
 """
from django.http import JsonResponse

""" @api_view(['POST'])
def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = respond_to_message_nlp(message)
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'error': 'Invalid request method'})
 """

from django.shortcuts import render
from django.http import JsonResponse
from Conversation.nlp_model import generate_response

""" @csrf_exempt
@api_view(['POST'])
def chat(request ):
    if request.method == 'POST':
        message = request.POST.get('message')
        print('message de requette ' , message )
        response = generate_response(message)
        return Response({'response': response})
    else:
        return Response({'error': 'Invalid request method'})
        
    # Pour les requêtes GET, renvoyer une réponse vide
   """  


""" @api_view(['POST'])
def chat(request):
    message = request.data.get('message')
    if message is None:
        return Response({'error': 'Le champ "message" est manquant dans la requête POST.'}, status=400)
    else:
        print('Message du chat :', message)
        response = generate_response(message)
        print('Réponse du chat :', response)
        return Response({'response': response})
 """

# views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .generative_ai import generate_response

# views.py

# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .generative_ai import generate_response

@api_view(['POST'])
def chat(request):
    message = request.data.get('message')
    if message is None:
        return Response({'error': 'Le champ "message" est manquant dans la requête POST.'}, status=400)
    else:
        print('Message du chat :', message)
        response = generate_response(message)
        print('Réponse du chat :', response)
        return Response({'response': response})
