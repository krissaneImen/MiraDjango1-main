from django.http import JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .models import ClassSchedule
from rest_framework.decorators import api_view

@api_view(['POST'])
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            annee_universitaire = form.cleaned_data['anneeUniversitaire']
            semestre = form.cleaned_data['semestre']
            classes = form.cleaned_data['classes']
            type = form.cleaned_data['type']
            emploi_file = form.cleaned_data['emploiFile']
            
            # Saving uploaded file to the database
            class_schedule = ClassSchedule(
                anneeUniversitaire=annee_universitaire,
                semestre=semestre,
                classes=classes,
                type=type,
                emploiFile=emploi_file
            )
            class_schedule.save()
            
            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(class_schedule.id),  # Convert ObjectId to string
                'anneeUniversitaire': class_schedule.anneeUniversitaire,
                'semestre': class_schedule.semestre,
                'classes': class_schedule.classes,
                'type': class_schedule.type,
                'emploiFile': str(class_schedule.emploiFile)  # Convert GridFSProxy to string
            })
    else:
        form = UploadFileForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})


# Django View for File Download
from django.http import HttpResponse, Http404
from .models import ClassSchedule


# emploi/views.py

from django.http import HttpResponse
from .models import ClassSchedule


def download_pdf(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        class_schedule = ClassSchedule.objects.get(pk=pk)
    except ClassSchedule.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Class schedule not found", status=404)
    
    # Assuming emploiFile is the field that stores the PDF file
    pdf_file = class_schedule.emploiFile
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download
    response['Content-Disposition'] = 'attachment; filename="schedule.pdf"'
    
    return response


# Django View for retrieving employment by ID
from django.http import JsonResponse
from .models import ClassSchedule

@api_view(['GET'])
def get_employment_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        class_schedule = ClassSchedule.objects.get(pk=pk)
    except ClassSchedule.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employment data to JSON response
    employment_data = {
        'id': str(class_schedule.id),
        'anneeUniversitaire': class_schedule.anneeUniversitaire,
        'semestre': class_schedule.semestre,
        'classes': class_schedule.classes,
        'type': class_schedule.type,
        'emploiFile': str(class_schedule.emploiFile)
    }
    
    return JsonResponse(employment_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_employment_list(request):
    employments = ClassSchedule.objects.all()
    
    # Convert employments to JSON format
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'anneeUniversitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'classes': employment.classes,
            'type': employment.type,
            'emploiFile': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)



@api_view([ 'PUT'])
def update_employment(request, pk):
    try:
        class_schedule = ClassSchedule.objects.get(pk=pk)
    except ClassSchedule.DoesNotExist:
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    if  request.method == 'PUT':
        form = UploadFileForm(request.data, request.FILES)
        if form.is_valid():
            annee_universitaire = form.cleaned_data['anneeUniversitaire']
            semestre = form.cleaned_data['semestre']
            classes = form.cleaned_data['classes']
            type = form.cleaned_data['type']
            emploi_file = form.cleaned_data['emploiFile']

            class_schedule.anneeUniversitaire = annee_universitaire
            class_schedule.semestre = semestre
            class_schedule.classes = classes
            class_schedule.type = type
            class_schedule.emploiFile = emploi_file
            class_schedule.save()
            
            return JsonResponse({
                'id': str(class_schedule.id),
                'anneeUniversitaire': class_schedule.anneeUniversitaire,
                'semestre': class_schedule.semestre,
                'classes': class_schedule.classes,
                'type': class_schedule.type,
                'emploiFile': str(class_schedule.emploiFile)
            })

@api_view(['DELETE'])
def delete_employment(request, pk):
    try:
        class_schedule = ClassSchedule.objects.get(pk=pk)
    except ClassSchedule.DoesNotExist:
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    if request.method == 'DELETE':
        class_schedule.delete()
        return JsonResponse({"message": "Employment deleted successfully"}, status=200)



@api_view(['GET'])
def get_employment_by_type(request, emploi_type):
    try:
        # Retrieve the ClassSchedule objects filtered by type
        employments = ClassSchedule.objects.filter(type=emploi_type)
    except ClassSchedule.DoesNotExist:
        # If no objects are found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employments data to a list of JSON responses
    employment_list = []
    for employment in employments:
        employment_data = {
            'id': str(employment.id),
            'anneeUniversitaire': employment.anneeUniversitaire,
            'semestre': employment.semestre,
            'classes': employment.classes,
            'type': employment.type,
            'emploiFile': str(employment.emploiFile)
        }
        employment_list.append(employment_data)
    
    return JsonResponse(employment_list, safe=False)


from django.core.exceptions import ObjectDoesNotExist
def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        photocopie = ClassSchedule.objects.get(pk=pk)
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

