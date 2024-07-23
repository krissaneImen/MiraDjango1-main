from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import EmploiEnseignant
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            annee_universitaire = form.cleaned_data['anneeUniversitaire']
            semestre = form.cleaned_data['semestre']
            NomEnseignant = form.cleaned_data['NomEnseignant']
            CinEnseignant = form.cleaned_data['CinEnseignant']
            type = form.cleaned_data['type']
            emploi_file = request.FILES['emploiFile']
            # Check if any file is uploaded
            
            
            # Check if all required fields are filled
            if annee_universitaire and semestre and NomEnseignant and CinEnseignant and type:
                # Saving uploaded file to the database
                emploi_enseignant = EmploiEnseignant(
                    anneeUniversitaire=annee_universitaire,
                    semestre=semestre,
                    CinEnseignant=CinEnseignant,
                    NomEnseignant=NomEnseignant,
                    type=type,
                    emploiFile=emploi_file
                )
                emploi_enseignant.save()
                
                # Returning uploaded file data in JSON response
                return JsonResponse({
                    'id': str(emploi_enseignant.id),  # Convert ObjectId to string
                    'anneeUniversitaire': emploi_enseignant.anneeUniversitaire,
                    'semestre': emploi_enseignant.semestre,
                    'CinEnseignant': emploi_enseignant.CinEnseignant,
                    'NomEnseignant': emploi_enseignant.NomEnseignant,
                    'type': emploi_enseignant.type,
                    'emploiFile': str(emploi_enseignant.emploiFile) if emploi_enseignant.emploiFile else None  # Convert GridFSProxy to string
                })
            else:
                # Return error response if any required field is missing
                return JsonResponse({'error': 'Missing required fields'}, status=400)
                
    else:
        form = UploadFileForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})


def download_pdf(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        emploi_enseignant = EmploiEnseignant.objects.get(pk=pk)
    except EmploiEnseignant.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Class schedule not found", status=404)
    
    # Assuming emploiFile is the field that stores the PDF file
    pdf_file = emploi_enseignant.emploiFile
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download
    response['Content-Disposition'] = 'attachment; filename="schedule.pdf"'
    
    return response


@api_view(['GET'])
def get_employment_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        emploi_enseignant = EmploiEnseignant.objects.get(pk=pk)
    except EmploiEnseignant.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employment data to JSON response
    employment_data = {
        'id': str(emploi_enseignant.id),
        'anneeUniversitaire': emploi_enseignant.anneeUniversitaire,
        'semestre': emploi_enseignant.semestre,
        'CinEnseignant': emploi_enseignant.CinEnseignant,
        'NomEnseignant': emploi_enseignant.NomEnseignant,
        'type': emploi_enseignant.type,
        'emploiFile': str(emploi_enseignant.emploiFile)
    }
    
    return JsonResponse(employment_data)

@api_view(['GET'])
def get_employment_by_cin(request, cin):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        emploi_enseignant = EmploiEnseignant.objects.get(CinEnseignant=cin)
    except EmploiEnseignant.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employment data to JSON response
    employment_data = {
        'id': str(emploi_enseignant.id),
        'anneeUniversitaire': emploi_enseignant.anneeUniversitaire,
        'semestre': emploi_enseignant.semestre,
        'CinEnseignant': emploi_enseignant.CinEnseignant,
        'NomEnseignant': emploi_enseignant.NomEnseignant,
        'type': emploi_enseignant.type,
        'emploiFile': str(emploi_enseignant.emploiFile)
    }
    
    return JsonResponse(employment_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_employment_list(request):
    employments = EmploiEnseignant.objects.all()
    
    # Convert employments to JSON format
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'anneeUniversitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'CinEnseignant': employment.CinEnseignant,
            'NomEnseignant': employment.NomEnseignant,
            'type': employment.type,
            'emploiFile': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)



@api_view(['PUT'])
def update_employment(request, pk):
    try:
        emploi_enseignant = EmploiEnseignant.objects.get(pk=pk)
    except EmploiEnseignant.DoesNotExist:
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    if request.method == 'PUT':
        form = UploadFileForm(request.data, request.FILES)
        if form.is_valid():
            annee_universitaire = form.cleaned_data['anneeUniversitaire']
            semestre = form.cleaned_data['semestre']
            NomEnseignant = form.cleaned_data['NomEnseignant']
            CinEnseignant = form.cleaned_data['CinEnseignant']
            type = form.cleaned_data['type']
            emploi_file = form.cleaned_data['emploiFile']

            emploi_enseignant.anneeUniversitaire = annee_universitaire
            emploi_enseignant.semestre = semestre
            emploi_enseignant.NomEnseignant = NomEnseignant
            emploi_enseignant.CinEnseignant = CinEnseignant
            emploi_enseignant.type = type
            emploi_enseignant.emploiFile = emploi_file
            emploi_enseignant.save()
            
            return JsonResponse({
                'id': str(emploi_enseignant.id),
                'anneeUniversitaire': emploi_enseignant.anneeUniversitaire,
                'semestre': emploi_enseignant.semestre,
                'CinEnseignant': emploi_enseignant.CinEnseignant,
                'NomEnseignant': emploi_enseignant.NomEnseignant,
                'type': emploi_enseignant.type,
                'emploiFile': str(emploi_enseignant.emploiFile)
            })
        else:
            # Handle form validation errors
            return JsonResponse({"error": "Form validation failed"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Handle incorrect HTTP method
        return JsonResponse({"error": "Invalid HTTP method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_employment(request, pk):
    try:
        emploi_enseignant = EmploiEnseignant.objects.get(pk=pk)
    except EmploiEnseignant.DoesNotExist:
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    if request.method == 'DELETE':
        emploi_enseignant.delete()
        return JsonResponse({"message": "Employment deleted successfully"}, status=200)



@api_view(['GET'])
def get_employment_by_type(request, emploi_type):
    try:
        # Retrieve the ClassSchedule objects filtered by type
        employments = EmploiEnseignant.objects.filter(type=emploi_type)
    except EmploiEnseignant.DoesNotExist:
        # If no objects are found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employments data to a list of JSON responses
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'anneeUniversitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'CinEnseignant': employment.CinEnseignant,
            'NomEnseignant': employment.NomEnseignant,
            'type': employment.type,
            'emploiFile': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)


@api_view(['GET'])
def get_mon_emploi_by_type(request, cin, emploi_type):
    try:
        # Retrieve the ClassSchedule objects filtered by type and Cinenseignant
        employments = EmploiEnseignant.objects.filter(type=emploi_type, CinEnseignant=cin)
    except EmploiEnseignant.DoesNotExist:
        # If no objects are found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employments data to a list of JSON responses
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'anneeUniversitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'CinEnseignant': employment.CinEnseignant,
            'NomEnseignant': employment.NomEnseignant,
            'type': employment.type,
            'emploiFile': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)
@api_view(['GET'])
def extraire_emploi_par_type(request, emploi_type):
    """
    Retrieve employments by type.

    :param request: HTTP request
    :param emploi_type: Type of employment to retrieve
    :return: JSON response with employments data
    """
    try:
        # Retrieve the EmploiEnseignant objects filtered by type
        employments = EmploiEnseignant.objects.filter(type=emploi_type)
    except EmploiEnseignant.DoesNotExist:
        # If no objects are found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employments data to a list of JSON responses
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'annee_universitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'cin_enseignant': employment.CinEnseignant,
            'nom_enseignant': employment.NomEnseignant,
            'type': employment.type,
            'emploi_file': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)



from django.core.exceptions import ObjectDoesNotExist
def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = EmploiEnseignant.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = photocopie.emploiFile
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % photocopie.emploiFile.name
    
    return response

