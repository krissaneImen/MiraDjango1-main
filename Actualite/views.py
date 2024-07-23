from django.http import JsonResponse
from django.shortcuts import render
from .forms import ActualiteForm
from .models import Actualite
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse



@api_view(['POST'])
def create_actualite(request):
    if request.method == 'POST':
        form = ActualiteForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            anneeUniversitaire = form.cleaned_data['anneeUniversitaire']
            date = form.cleaned_data['date']
            intitule = form.cleaned_data['intitule']
            etudiant = form.cleaned_data['etudiant']
            enseignant = form.cleaned_data['enseignant']
            administratif = form.cleaned_data['administratif']
            administrateur = form.cleaned_data['administrateur']
            fichier = form.cleaned_data['fichier']
            
            # Saving uploaded file to the database
            actualite = Actualite(
                anneeUniversitaire=anneeUniversitaire,
                date=date,
                intitule=intitule,
                etudiant=etudiant,
                enseignant=enseignant,
                administratif=administratif,
                administrateur=administrateur,
                fichier=fichier
            )
            actualite.save()
            
            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(actualite.id),  # Convert ObjectId to string
                'anneeUniversitaire': actualite.anneeUniversitaire,
                'date': actualite.date,
                'intitule': actualite.intitule,
                'etudiant': actualite.etudiant,
                'enseignant': actualite.enseignant,
                'administratif': actualite.administratif,
                'administrateur': actualite.administrateur,
                'fichier': str(actualite.fichier)  # Convert GridFSProxy to string
            })
    else:
        form = ActualiteForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})



def download_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        actualite = Actualite.objects.get(pk=pk)
    except actualite.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("actualite not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = actualite.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{actualite.fichier.name}"'
    
    return response




def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        actualite = Actualite.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = actualite.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % actualite.fichier.name
    
    return response


# Django View for retrieving employment by ID

@api_view(['GET'])
def get_actualite_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        actualite = Actualite.objects.get(pk=pk)
    except Actualite.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "actualite not found"}, status=404)
    
    # Convert the employment data to JSON response
    actualite_data = {
        'id': str(actualite.id),
        'anneeUniversitaire': actualite.anneeUniversitaire,
        'date': actualite.date,
        'intitule': actualite.intitule,
        'etudiant': actualite.etudiant,
        'enseignant': actualite.enseignant,
        'administratif': actualite.administratif,
        'administrateur': actualite.administrateur,
        'fichier': str(actualite.fichier)
    }
    
    return JsonResponse(actualite_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_actualite_list(request):
    actualites = Actualite.objects.all()
    
    # Convert employments to JSON format
    actualite_list = []
    for actualite in actualites:
        actualite_data = {
            'id': str(actualite.id),
            'anneeUniversitaire': actualite.anneeUniversitaire,
            'date': actualite.date,
            'intitule': actualite.intitule,
            'etudiant': actualite.etudiant,
            'enseignant': actualite.enseignant,
            'administratif': actualite.administratif,
            'administrateur': actualite.administrateur,
            'fichier': str(actualite.fichier)
        }
        actualite_list.append(actualite_data)
    
    return JsonResponse(actualite_list, safe=False)



from django.http import JsonResponse
from django.utils import timezone
from .forms import ActualiteForm
from .models import Actualite

@api_view(['PUT'])
def update_actualite(request, pk):
    try:
        actualite = Actualite.objects.get(pk=pk)
    except Actualite.DoesNotExist:
        return JsonResponse({"error": "Actualite not found"}, status=404)
    
    if request.method == 'PUT':
        form = ActualiteForm(request.data, request.FILES)  
        if form.is_valid():
            actualite.anneeUniversitaire = form.cleaned_data['anneeUniversitaire']
            actualite.date = form.cleaned_data['date']
            actualite.intitule = form.cleaned_data['intitule']
            actualite.etudiant = form.cleaned_data['etudiant']
            actualite.enseignant = form.cleaned_data['enseignant']
            actualite.administratif = form.cleaned_data['administratif']
            actualite.administrateur = form.cleaned_data['administrateur']
            
            # Check if a new file is provided
            if 'fichier' in request.FILES:
                actualite.fichier = request.FILES['fichier']
            else:
                # Optionally handle the case where no new file is provided
                pass

            actualite.save()

            return JsonResponse({
                'id': str(actualite.id),
                'anneeUniversitaire': actualite.anneeUniversitaire,
                'date': actualite.date,
                'intitule': actualite.intitule,
                'etudiant': actualite.etudiant,
                'enseignant': actualite.enseignant,
                'administratif': actualite.administratif,
                'administrateur': actualite.administrateur,
                'fichier': str(actualite.fichier)
            })
        else:
            return JsonResponse(form.errors, status=400)  # Return form errors if form is invalid
    else:
        return JsonResponse({"error": "PUT method required"}, status=405)  # Return method not allowed error for non-PUT requests



@api_view(['DELETE'])
def delete_actualite(request, pk):
    try:
        actualite = Actualite.objects.get(pk=pk)
    except Actualite.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if request.method == 'DELETE':
        actualite.delete()
        return JsonResponse({"message": "actualite deleted successfully"}, status=200)


""" @api_view(['GET'])
def get_actualite_list_by_cin(request, cin):
    try:
        # Retrieve the list of Photocopie objects by cin
        photocopies = Actualite.objects.filter(cin=cin)
    except Actualite.DoesNotExist:
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

 """

from django.core.exceptions import ObjectDoesNotExist
def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = Actualite.objects.get(pk=pk)
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

@api_view(['GET'])
def get_all_actualite(request, userType):
    """
    Get all actualites based on user type.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - userType: str - type of the user (etudiant, enseignant, administratif, administrateur).

    Returns:
    - Response: JSON response with filtered actualites data.
    """
    if request.method == 'GET':
        # Filter actualites based on userType
        if userType == 'etudiant':
            actualites = Actualite.objects.filter(etudiant=True)
        elif userType == 'enseignant':
            actualites = Actualite.objects.filter(enseignant=True)
        elif userType == 'administratif':
            actualites = Actualite.objects.filter(administratif=True)
        elif userType == 'administrateur':
            actualites = Actualite.objects.filter(administrateur=True)
        else:
            return Response({"error": "Invalid userType"}, status=status.HTTP_400_BAD_REQUEST)

        # Manually construct serialized data from queryset
        actualite_list = []
        for actualite in actualites:
            actualite_data = {
                'id': str(actualite.id),
                'anneeUniversitaire': actualite.anneeUniversitaire,
                'date': actualite.date,
                'intitule': actualite.intitule,
                'etudiant': actualite.etudiant,
                'enseignant': actualite.enseignant,
                'administratif': actualite.administratif,
                'administrateur': actualite.administrateur,
                'fichier': str(actualite.fichier)
            }
            actualite_list.append(actualite_data)

        return Response(actualite_list, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
