from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from Soutenance.models import Soutenance
from .forms import RapportForm
from .models import Rapport
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from rest_framework import status




@api_view(['POST'])
def create_Rapport(request):
    form = RapportForm(request.POST, request.FILES)
    if form.is_valid():
        # Extracting data from the form
        Cin = form.cleaned_data['Cin']
        anneeUniversitaire = form.cleaned_data['anneeUniversitaire']
        Titre = form.cleaned_data['Titre']
        NatureStage = form.cleaned_data['NatureStage']
        Version = form.cleaned_data['Version']
        NomEtudiant = form.cleaned_data['NomEtudiant']
        CinRaporteur = form.cleaned_data['CinRaporteur']
        NomRaporteur = form.cleaned_data['NomRaporteur']
        rapport_file = form.cleaned_data['Rapport']  # Changed variable name

        # Saving uploaded file to the database
        Rap = Rapport(
            Cin=Cin,
            anneeUniversitaire=anneeUniversitaire,
            Titre=Titre,
            NatureStage=NatureStage,
            Version=Version,
            NomEtudiant=NomEtudiant,
            CinRaporteur=CinRaporteur,
            NomRaporteur=NomRaporteur,
            Rapport=rapport_file  # Assigning to the correct field
        )
        Rap.save()

        # Returning uploaded file data in JSON response
        return JsonResponse({
            'id': str(Rap.id),  # Convert ObjectId to string
            'Cin': Rap.Cin,
            'anneeUniversitaire': Rap.anneeUniversitaire,
            'Titre': Rap.Titre,
            'NatureStage': Rap.NatureStage,
            'Version': Rap.Version,
            'NomEtudiant': Rap.NomEtudiant,
            'CinRaporteur': Rap.CinRaporteur,
            'NomRaporteur': Rap.NomRaporteur,
            'Rapport': str(Rap.Rapport)  # Convert the file path to string
        })
    else:
        # Return form errors
        return JsonResponse({'errors': form.errors}, status=400)


def download_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        rapport = Rapport.objects.get(pk=pk)
    except Rapport.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = rapport.Rapport
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{rapport.Rapport.name}"'
    
    return response

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        rapport = Rapport.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = rapport.Rapport
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % rapport.Rapport.name
    
    return response


# Django View for retrieving employment by ID

@api_view(['GET'])
def get_Rapport_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        rapport = Rapport.objects.get(pk=pk)
    except Rapport.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    # Convert the employment data to JSON response
    Rapport_data = {
        'id': str(rapport.id),
        'Cin': rapport.Cin,
        'anneeUniversitaire': rapport.anneeUniversitaire,
        
        'Titre': rapport.Titre,
        'NatureStage': rapport.NatureStage,
        'Version': rapport.Version,
        'NomEtudiant': rapport.NomEtudiant,
        'NomRaporteur': rapport.NomRaporteur,
        'CinRaporteur': rapport.CinRaporteur,
        'Rapport': str(rapport.Rapport)
    }
    
    return JsonResponse(Rapport_data)





# Django View for retrieving the list of employments
@api_view(['GET'])
def get_Rapport_list(request):
    rapports = Rapport.objects.all()
    
    # Convert employments to JSON format
    rapport_list = []
    for rapport in rapports:
        rapport_data = {
            'id': str(rapport.id),
            'Cin': rapport.Cin,
            'anneeUniversitaire': rapport.anneeUniversitaire,
            'Titre': rapport.Titre,
            'NatureStage': rapport.NatureStage,
            'Version': rapport.Version,
            'NomEtudiant': rapport.NomEtudiant,
            'NomRaporteur': rapport.NomRaporteur,
            'CinRaporteur': rapport.CinRaporteur,
            'Rapport': str(rapport.Rapport)
        }
        rapport_list.append(rapport_data)
    
    return JsonResponse(rapport_list, safe=False)




@api_view(['PUT'])
def update_Rapport(request, pk):
    try:
        rapport_instance = Rapport.objects.get(pk=pk)
    except Rapport.DoesNotExist:
        return JsonResponse({"error": "Rapport not found"}, status=404)
    
    if request.method == 'PUT':
        form = RapportForm(request.data, request.FILES)
        if form.is_valid():
            Cin = form.cleaned_data['Cin']
            anneeUniversitaire = form.cleaned_data['anneeUniversitaire']
            Titre = form.cleaned_data['Titre']
            NatureStage = form.cleaned_data['NatureStage']
            Version = form.cleaned_data['Version']
            NomEtudiant = form.cleaned_data['NomEtudiant']
            NomRaporteur = form.cleaned_data['NomRaporteur']
            CinRaporteur = form.cleaned_data['CinRaporteur']
            RapportFile = form.cleaned_data['Rapport']  # Renamed variable to avoid conflict

            rapport_instance.Cin = Cin
            rapport_instance.anneeUniversitaire = anneeUniversitaire
            rapport_instance.Titre = Titre
            rapport_instance.NatureStage = NatureStage
            rapport_instance.Version = Version
            rapport_instance.NomEtudiant = NomEtudiant
            rapport_instance.NomRaporteur = NomRaporteur
            rapport_instance.CinRaporteur = CinRaporteur
            rapport_instance.Rapport = RapportFile  # Updated variable assignment
            rapport_instance.save()
            
            return JsonResponse({
                'id': str(rapport_instance.id),
                'Cin': rapport_instance.Cin,
                'anneeUniversitaire': rapport_instance.anneeUniversitaire,
                'Titre': rapport_instance.Titre,
                'NatureStage': rapport_instance.NatureStage,
                'Version': rapport_instance.Version,
                'NomEtudiant': rapport_instance.NomEtudiant,
                'NomRaporteur': rapport_instance.NomRaporteur,
                'CinRaporteur': rapport_instance.CinRaporteur,
                'Rapport': str(rapport_instance.Rapport)
            })
        else:
            return JsonResponse({"error": "Form data is not valid", "details": form.errors}, status=400)
    
    return JsonResponse({"error": "Invalid HTTP method"}, status=405)



@api_view(['DELETE'])
def delete_Rapport(request, pk):
    try:
        rapport = Rapport.objects.get(pk=pk)
    except Rapport.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if request.method == 'DELETE':
        rapport.delete()
        return JsonResponse({"message": "photocopie deleted successfully"}, status=200)


@api_view(['GET'])
def get_Rapport_list_by_cin(request, cin):
    try:
        # Retrieve the list of Photocopie objects by cin
        rapports = Rapport.objects.filter(Cin=cin)
    except Rapport.DoesNotExist:
        # If no Photocopie objects are found for the given cin, return an appropriate response
        return JsonResponse({"error": "No photocopie found for the provided cin"}, status=404)
    
    # Convert photocopie data to JSON format
    rapports_list = []
    for rapport in rapports:
        rapport_data = {
            'id': str(rapport.id),
            'Cin': rapport.Cin,
            'anneeUniversitaire': rapport.anneeUniversitaire,
            
            'Titre': rapport.Titre,
            'NatureStage': rapport.NatureStage,
            'Version': rapport.Version,
            'NomEtudiant': rapport.NomEtudiant,
            'NomRaporteur': rapport.NomRaporteur,
            'CinRaporteur': rapport.CinRaporteur,
            'Rapport': str(rapport.Rapport)
        }
        rapports_list.append(rapport_data)
    
    return JsonResponse(rapports_list, safe=False)


@api_view(['GET'])
def get_students_by_president_jury_cin(request, cin_president_jury):
    try:
        # Filtrer les soutenances par le CIN du président du jury
        soutenances = Soutenance.objects.filter(CinRaporteur=cin_president_jury)

        # Vérifier si des soutenances ont été trouvées
        if soutenances:
            # Extraire les CIN des étudiants associés à ces soutenances
            students_cins = set()
            for soutenance in soutenances:
                for etudiant in soutenance.Etudiants:
                    students_cins.add(etudiant.Cin)

            # Récupérer les journaux des étudiants
            rapports = Rapport.objects.filter(Cin__in=students_cins)
    
            # Convertir les rapports en format JSON
            rapport_list = []
            for rapport in rapports:
                rapport_data = {
                    'id': str(rapport.id),
                    'Cin': rapport.Cin,
                    'anneeUniversitaire': rapport.anneeUniversitaire,
                    'Titre': rapport.Titre,
                    'NatureStage': rapport.NatureStage,
                    'Version': rapport.Version,
                    'NomEtudiant': rapport.NomEtudiant,
                    'NomRaporteur': rapport.NomRaporteur,
                    'CinRaporteur': rapport.CinRaporteur,
                    'Rapport': str(rapport.Rapport)
                }
                rapport_list.append(rapport_data)
    
            return Response(rapport_list, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Aucune soutenance trouvée pour ce président de jury"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



