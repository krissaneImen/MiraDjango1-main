from django.http import JsonResponse
from django.shortcuts import render
from .forms import PhotocopieForm
from .models import Photocopie
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse


@api_view(['POST'])
def create_photocopie(request):
    if request.method == 'POST':
        form = PhotocopieForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            cin = form.cleaned_data['cin']
            idDemande = form.cleaned_data['idDemande']
            nombreCopie = form.cleaned_data['nombreCopie']
            NomEnseignant = form.cleaned_data['NomEnseignant']
            cour = form.cleaned_data['cour']
            fichier = form.cleaned_data['fichier']
            
            # Saving uploaded file to the database
            Demande_Photocopie = Photocopie(
                cin=cin,
                idDemande=idDemande,
                nombreCopie=nombreCopie,
                NomEnseignant=NomEnseignant,
                cour=cour,
                fichier=fichier
            )
            Demande_Photocopie.save()
            
            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(Demande_Photocopie.id),  # Convert ObjectId to string
                'cin': Demande_Photocopie.cin,
                'idDemande': Demande_Photocopie.idDemande,
                'nombreCopie': Demande_Photocopie.nombreCopie,
                'NomEnseignant': Demande_Photocopie.NomEnseignant,
                'cour': Demande_Photocopie.cour,
                'fichier': str(Demande_Photocopie.fichier)  # Convert GridFSProxy to string
            })
    else:
        form = PhotocopieForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})


# Django View for File Download


def download_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = Photocopie.objects.get(pk=pk)
    except Photocopie.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = photocopie.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{photocopie.fichier.name}"'
    
    return response

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = Photocopie.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = photocopie.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % photocopie.fichier.name
    
    return response


# Django View for retrieving employment by ID

@api_view(['GET'])
def get_photocopie_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        photocopie = Photocopie.objects.get(pk=pk)
    except Photocopie.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    # Convert the employment data to JSON response
    photocopie_data = {
        'id': str(photocopie.id),
        'cin': photocopie.cin,
        'nombreCopie': photocopie.nombreCopie,
        'NomEnseignant': photocopie.NomEnseignant,
        'cour': photocopie.cour,
        'fichier': str(photocopie.fichier)
    }
    
    return JsonResponse(photocopie_data)

@api_view(['GET'])
def get_photocopie_by_Demande(request, idDemande):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        photocopie = Photocopie.objects.get(idDemande=idDemande)
    except Photocopie.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    # Convert the employment data to JSON response
    photocopie_data = {
        'id': str(photocopie.id),
        'cin': photocopie.cin,
        'nombreCopie': photocopie.nombreCopie,
        'NomEnseignant': photocopie.NomEnseignant,
        'cour': photocopie.cour,
        'fichier': str(photocopie.fichier)
    }
    
    return JsonResponse(photocopie_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_photocopie_list(request):
    photocopies = Photocopie.objects.all()
    
    # Convert employments to JSON format
    photocopies_list = []
    for photocopie in photocopies:
        photocopie_data = {
            'id': str(photocopie.id),
            'cin': photocopie.cin,
            'idDemande': photocopie.idDemande,
            'nombreCopie': photocopie.nombreCopie,
            'NomEnseignant': photocopie.NomEnseignant,
            'cour': photocopie.cour,
            'fichier': str(photocopie.fichier)
        }
        photocopies_list.append(photocopie_data)
    
    return JsonResponse(photocopies_list, safe=False)



@api_view([ 'PUT'])
def update_photocopie(request, pk):
    try:
        photocopie = Photocopie.objects.get(pk=pk)
    except Photocopie.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if  request.method == 'PUT':
        form = PhotocopieForm(request.data, request.FILES)
        if form.is_valid():
            cin = form.cleaned_data['cin']
            idDemande = form.cleaned_data['idDemande']
            nombreCopie = form.cleaned_data['nombreCopie']
            NomEnseignant = form.cleaned_data['NomEnseignant']
            cour = form.cleaned_data['cour']
            fichier = form.cleaned_data['fichier']

            photocopie.cin = cin
            photocopie.idDemande = idDemande
            photocopie.nombreCopie = nombreCopie
            photocopie.NomEnseignant = NomEnseignant
            photocopie.cour = cour
            photocopie.fichier = fichier
            photocopie.save()
            
            return JsonResponse({
                'id': str(photocopie.id),
                'cin': photocopie.cin,
                'idDemande': photocopie.idDemande,
                'nombreCopie': photocopie.nombreCopie,
                'NomEnseignant': photocopie.NomEnseignant,
                'cour': photocopie.cour,
                'fichier': str(photocopie.fichier)
            })

@api_view(['DELETE'])
def delete_photocopie(request, pk):
    try:
        photocopie = Photocopie.objects.get(pk=pk)
    except Photocopie.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if request.method == 'DELETE':
        photocopie.delete()
        return JsonResponse({"message": "photocopie deleted successfully"}, status=200)


@api_view(['GET'])
def get_photocopie_list_by_cin(request, cin):
    try:
        # Retrieve the list of Photocopie objects by cin
        photocopies = Photocopie.objects.filter(cin=cin)
    except Photocopie.DoesNotExist:
        # If no Photocopie objects are found for the given cin, return an appropriate response
        return JsonResponse({"error": "No photocopie found for the provided cin"}, status=404)
    
    # Convert photocopie data to JSON format
    photocopies_list = []
    for photocopie in photocopies:
        photocopie_data = {
            'id': str(photocopie.id),
            'cin': photocopie.cin,
            'idDemande': photocopie.idDemande,
            'nombreCopie': photocopie.nombreCopie,
            'NomEnseignant': photocopie.NomEnseignant,
            'cour': photocopie.cour,
            'fichier': str(photocopie.fichier)
        }
        photocopies_list.append(photocopie_data)
    
    return JsonResponse(photocopies_list, safe=False)

