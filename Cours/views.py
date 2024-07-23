from django.http import JsonResponse
import spacy
from django.http import JsonResponse
from django.shortcuts import render
from .forms import SupportForm
from .models import SupportCours
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from PyPDF2 import PdfReader
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import requests
from bs4 import BeautifulSoup
import json


def getResume(request, pk):
    try:
        # Retrieve the Actualite object by its primary key (pk)
        supportCour = SupportCours.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Support Cours not found", status=404)

    # Assuming fichier is the field that stores the PDF file
    pdf_file = supportCour.Support
    try:
        reader = PdfReader(pdf_file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        parser = PlaintextParser.from_string(text, Tokenizer("french"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count=1)
        topic = str(summary[0])
        topic = ' '.join(str(sentence) for sentence in summary)
        return HttpResponse( topic)
        return JsonResponse({'topic': topic})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def create_Support(request):
    if request.method == 'POST':
        form = SupportForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            Titre = form.cleaned_data['Titre']
            DateAjout = form.cleaned_data['DateAjout']
            Description = form.cleaned_data['Description']
            Support = form.cleaned_data['Support']

            # Saving uploaded file to the database
            supportCour = SupportCours(
                Titre=Titre,
                DateAjout=DateAjout,
                Description=Description,
                Support=Support
            )
            supportCour.save()

            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(supportCour.id),  # Convert ObjectId to string
                'Titre': supportCour.Titre,
                'DateAjout': supportCour.DateAjout,
                'Description': supportCour.Description,
                'Support': str(supportCour.Support)  # Convert GridFSProxy to string
            })
    else:
        form = SupportForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})

def download_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        supportCour = SupportCours.objects.get(pk=pk)
    except supportCour.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("actualite not found", status=404)

    # Assuming fichier is the field that stores the PDF file
    pdf_file = supportCour.Support

    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')

    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{supportCour.Support.name}"'

    return response 

def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        supportCour = SupportCours.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)

    # Assuming fichier is the field that stores the PDF file
    pdf_file = supportCour.Support

    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')

    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{supportCour.Support.name}"'

    return response 

@api_view(['GET'])
def get_Support_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        supportCour = SupportCours.objects.get(pk=pk)
    except SupportCours.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "actualite not found"}, status=404)

    # Convert the employment data to JSON response
    supportCour_data = {
        'id': str(supportCour.id),
        'Titre': supportCour.Titre,
        'DateAjout': supportCour.DateAjout,
        'Description': supportCour.Description,
        'Support': str(supportCour.Support)
    }

    return JsonResponse(supportCour_data)

# Django View for retrieving the list of employments
@api_view(['GET'])
def get_support_list(request):
    supportsCour = SupportCours.objects.all()

    # Convert employments to JSON format
    supportCour_list = []
    for supportCour in supportsCour:
        supportCour_data = {
            'id': str(supportCour.id),
            'Titre': supportCour.Titre,
            'DateAjout': supportCour.DateAjout,
            'Description': supportCour.Description,
            'Support': str(supportCour.Support)
        }
        supportCour_list.append(supportCour_data)

    return JsonResponse(supportCour_list, safe=False)

@api_view(['PUT'])
def update_support(request, pk):
    try:
        supportCour = SupportCours.objects.get(pk=pk)
    except SupportCours.DoesNotExist:
        return JsonResponse({"error": "Actualite not found"}, status=404)

    if request.method == 'PUT':
        form = SupportCours(request.data, request.FILES)  
        if form.is_valid():
            supportCour.Titre = form.cleaned_data['Titre']
            supportCour.DateAjout = form.cleaned_data['DateAjout']
            supportCour.Description = form.cleaned_data['Description']

            # Check if a new file is provided
            if 'Support' in request.FILES:
                supportCour.Support = request.FILES['Support']
            else:
                # Optionally handle the case where no new file is provided
                pass

            supportCour.save()

            return JsonResponse({
                'id': str(supportCour.id),
                'Titre': supportCour.Titre,
                'DateAjout': supportCour.DateAjout,
                'Description': supportCour.Description,
                'Support': str(supportCour.Support)
            })
        else:
            return JsonResponse(form.errors, status=400)  # Return form errors if form is invalid
    else:
        return JsonResponse({"error": "PUT method required"}, status=405)  # Return method not allowed error for non-PUT requests

@api_view(['DELETE'])
def delete_support(request, pk):
    try:
        supportCour = SupportCours.objects.get(pk=pk)
    except SupportCours.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)

    if request.method == 'DELETE':
        supportCour.delete()
        return JsonResponse({"message": "actualite deleted successfully"}, status=200)

""" 
def scrape_stack_overflow_question(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extraire le titre de la question
        question_title_element = soup.find(id='question-header')
        if question_title_element:
            question_title = question_title_element.text.strip()
        else:
            question_title = "Titre de la question non trouvé"

        # Extraire le corps de la question
        question_body_element = soup.find('div', class_='question').find('div', class_='s-prose js-post-body')
        if question_body_element:
            question_body = question_body_element.text.strip()
        else:
            question_body = "Corps de la question non trouvé"

        # Extraire les balises
        tags_elements = soup.find_all('a', class_='post-tag')
        tags = [tag.text.strip() for tag in tags_elements]

        # Extraire toutes les réponses
        answers = []
        answer_elements = soup.find_all('div', class_='s-prose js-post-body')
        for answer_element in answer_elements:
            answer_body = answer_element.text.strip()
            answers.append(answer_body)

        return {
            "question_title": question_title,
            "question_body": question_body,
            "tags": tags,
            "answers": answers
        }
    else:
        print("La requête a échoué.")
        return None

# Fonction pour récupérer les URLs des 20 premières questions de Stack Overflow
def get_question_urls():
    base_url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "site": "stackoverflow",
        "pagesize": 20,  # Nombre de questions à récupérer
        "order": "desc",
        "sort": "creation"  # Tri par date de création
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        question_urls = [item['link'] for item in data['items']]
        return question_urls
    else:
        print("La requête a échoué.")
        return None

# Liste des URLs des 20 premières questions de Stack Overflow
question_urls = get_question_urls()

question_data_list = []
for url in question_urls:
    question_data = scrape_stack_overflow_question(url)
    if question_data:
        question_data_list.append(question_data)

# Enregistrer les données dans un fichier JSON
if question_data_list:
    with open('stack_overflow_data.json', 'w', encoding='utf-8') as file:
        json.dump(question_data_list, file, ensure_ascii=False, indent=4)
 """
# Charger les données JSON
def load_responses_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Charger les données JSON à partir du fichier créé précédemment
responses_data = load_responses_from_json('/Users/zitouni/python_stuff/MiraDjango1-main/stack_overflow_data.json')

# Charger le modèle SpaCy
nlp = spacy.load("fr_core_news_sm")

# Fonction pour répondre au message en utilisant NLP
def respond_to_message_nlp(message):
    if message is None:
        return "Veuillez fournir un message valide."
    else:
        doc = nlp(message)
    
    # Extraire les entités nommées du message (pas nécessaire pour le moment)
    entities = [ent.text for ent in doc.ents]
    
    # Générer une réponse basée sur la similarité avec les questions existantes
    response = generate_response(message)
    
    return response

# Fonction pour générer une réponse basée sur la similarité avec les questions existantes
def generate_response(user_question):
    # Calculez la similarité entre la question de l'utilisateur et chaque question dans les données
    similarities = [(question['question_title'], compute_similarity(user_question, question['question_title'])) for question in responses_data]
    
    # Trier les similarités par ordre décroissant
    sorted_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    
    # Sélectionnez la question la plus similaire
    most_similar_question = sorted_similarities[0][0]
    
    # Recherchez la réponse correspondant à la question la plus similaire
    response = next((question['answers'][0] for question in responses_data if question['question_title'] == most_similar_question), None)
    
    if response:
        return response
    else:
        return "Je suis désolé, je ne sais pas comment répondre à cela."

def compute_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


@api_view(['POST'])
def chat(request):
    message = request.data.get('message')
    if message is None:
        return Response({'error': 'Le champ "message" est manquant dans la requête POST.'}, status=400)
    else:
        print('Message du chat :', message)
        response = respond_to_message_nlp(message)
        print('Réponse du chat :', response)
        return Response({'response': response})


from PyPDF2 import PdfReader
import json

def extract_pdf_data(request, pk):
    try:
        # Récupérer le document PDF par son ID
        supportCour = SupportCours.objects.get(pk=pk)
    except SupportCours.DoesNotExist:
        # Si le document n'est pas trouvé, retourner une réponse appropriée
        return JsonResponse({"error": "PDF not found"}, status=404)

    # Lire le contenu du PDF
    try:
        reader = PdfReader(supportCour.Support)
        data = {"Titre": supportCour.Titre, "Contenu": {}}

        # Variables pour suivre le titre et le paragraphe actuels
        current_title = None
        current_paragraph = ""

        # Parcourir chaque page du PDF
        for page_number, page in enumerate(reader.pages, start=1):
            # Extraire le texte de la page
            page_text = page.extract_text()

            # Diviser le texte en lignes
            lines = page_text.split("\n")

            # Parcourir chaque ligne de la page
            for line in lines:
                # Vérifier si la ligne est un titre (vous devez ajuster cette condition en fonction de la structure de vos titres)
                if line.isupper():  # Par exemple, vérifier si la ligne est en majuscules
                    # Si un titre précédent existe, enregistrer le titre et le paragraphe actuels
                    if current_title and current_paragraph:
                        data["Contenu"][current_title] = current_paragraph.strip()
                    
                    # Mettre à jour le titre actuel
                    current_title = line.strip()
                    # Réinitialiser le paragraphe actuel
                    current_paragraph = ""
                else:
                    # Ajouter la ligne au paragraphe actuel
                    current_paragraph += line.strip() + " "
            
            # Enregistrer le dernier titre et paragraphe de la page
            if current_title and current_paragraph:
                data["Contenu"][current_title] = current_paragraph.strip()

        # Enregistrer les données dans un fichier JSON
        file_path = f"{supportCour.Titre}.json"
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        # Retourner le chemin du fichier JSON
        return JsonResponse({"file_path": file_path})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
