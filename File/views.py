from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PDFFile
from .serializers import PDFFileSerializer

@api_view(['POST'])
def pdf_file_create(request):
    if request.method == 'POST':
        name = request.data.get('name')
        pdf_file = request.FILES.get('pdf_file')
        type = request.data.get('type')
        etudiantCible = request.data.get('etudiant') == 'true'  # Convertir en booléen
        enseignantCible = request.data.get('enseignant') == 'true'  # Convertir en booléen
        administrateurCible = request.data.get('administrateur') == 'true'  # Convertir en booléen
        administratifCible = request.data.get('administratif') == 'true'  # Convertir en booléen

        if not name or not pdf_file:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        # Création d'une nouvelle instance de PDFFile avec les données reçues
        new_pdf_file = PDFFile(
            name=name,
            type=type,
            pdf_file=pdf_file,
            etudiant=etudiantCible,
            enseignant=enseignantCible,
            administrateur=administrateurCible,
            administratif=administratifCible
        )
        new_pdf_file.save()

        # Sérialisation de l'objet PDFFile nouvellement créé
        serialized_data = PDFFileSerializer(new_pdf_file).data

        # Retourner les données sérialisées avec un statut de réussite
        return Response(serialized_data, status=status.HTTP_201_CREATED)
    else:
        # Retourner une réponse indiquant que la méthode n'est pas autorisée pour toute autre méthode HTTP
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    


@api_view(['GET'])
def pdf_file_list(request):
    if request.method == 'GET':
        pdf_files = PDFFile.objects.all()
        serialized_data = PDFFileSerializer(pdf_files, many=True).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def pdf_file_detail(request, pk):
    try:
        pdf_file = PDFFile.objects.get(pk=pk)
    except PDFFile.DoesNotExist:
        return Response({'error': 'PDF file not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized_data = PDFFileSerializer(pdf_file).data
        return Response(serialized_data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        # Logique pour mettre à jour l'enregistrement PDF
        pass
    elif request.method == 'DELETE':
        # Logique pour supprimer l'enregistrement PDF
        pass
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def get_all_files(request):
    if request.method == 'GET':
        # Récupérer tous les fichiers PDF de la base de données
        pdf_files = PDFFile.objects.all()
        # Sérialiser les données des fichiers PDF
        serialized_data = PDFFileSerializer(pdf_files, many=True).data
        # Retourner les données sérialisées avec un statut de réussite
        return Response(serialized_data, status=status.HTTP_200_OK)
    else:
        # Retourner une réponse indiquant que la méthode n'est pas autorisée pour toute autre méthode HTTP
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_file_by_id(request, file_id):
    if request.method == 'GET':
        try:
            # Récupérer le fichier PDF par son ID
            pdf_file = PDFFile.objects.get(pk=file_id)
            # Sérialiser les données du fichier PDF
            serialized_data = PDFFileSerializer(pdf_file).data
            # Retourner les données sérialisées avec un statut de réussite
            return Response(serialized_data, status=status.HTTP_200_OK)
        except PDFFile.DoesNotExist:
            # Retourner une réponse avec une erreur indiquant que le fichier n'existe pas
            return Response({'error': 'PDF File not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        # Retourner une réponse indiquant que la méthode n'est pas autorisée pour toute autre méthode HTTP
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PDFFile
from .serializers import PDFFileSerializer

# Vue pour afficher la liste de tous les fichiers PDF avec la possibilité de les télécharger
@api_view(['GET'])
def file_list_view(request):
    if request.method == 'GET':
        try:
            # Récupérer tous les fichiers PDF de la base de données
            pdf_files = PDFFile.objects.all()
            # Sérialiser les données des fichiers PDF
            serialized_data = PDFFileSerializer(pdf_files, many=True).data
            return render(request, 'file_list.html', {'files': serialized_data})
        except PDFFile.DoesNotExist:
            return Response({'error': 'No PDF files found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Vue pour télécharger un fichier PDF par son ID
import base64
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import PDFFile
import base64

@api_view(['GET'])
def download_file_view(request, name):
    if request.method == 'GET':
        try:
            # Retrieve the PDF file by its ID
            pdf_file = PDFFile.objects.get(name=name)
            
            # Read the PDF file content
            pdf_content = pdf_file.pdf_file.read()
            
            # Encode the PDF content as base64
            pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
            
            # Return the base64-encoded PDF content in the response
            return Response({'pdf_base64': pdf_base64}, status=status.HTTP_200_OK)
        except PDFFile.DoesNotExist:
            return Response({'error': 'PDF File not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
