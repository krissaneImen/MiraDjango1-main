from django.http import JsonResponse
from django.shortcuts import render
from .forms import CalandrierForm
from .models import Calandrier
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
def create_Calendrier(request):
    if request.method == 'POST':
        form = CalandrierForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            Nom = form.cleaned_data['Nom']
            semestre = form.cleaned_data['semestre']
            AU = form.cleaned_data['AU']
            fichier = form.cleaned_data['fichier']
            
            # Saving uploaded file to the database
            calandrier = Calandrier(
                Nom=Nom,
                semestre=semestre,
                AU=AU,
                fichier=fichier
            )
            calandrier.save()
            
            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(calandrier.id),  # Convert ObjectId to string
                'Nom': calandrier.Nom,
                'semestre': calandrier.semestre,
                'AU': calandrier.AU,
                'fichier': str(calandrier.fichier)  # Convert GridFSProxy to string
            })
    else:
        form = CalandrierForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})


# Django View for File Download


def download_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        calandrier = Calandrier.objects.get(pk=pk)
    except Calandrier.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = calandrier.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download and use the filename from the database
    response['Content-Disposition'] = f'attachment; filename="{calandrier.fichier.name}"'
    
    return response


def open_pdf(request, pk):
    try:
        # Retrieve the Photocopie object by its primary key (pk)
        calandrier = Calandrier.objects.get(pk=pk)
    except ObjectDoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = calandrier.fichier
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % calandrier.fichier.name
    
    return response


# Django View for retrieving employment by ID

@api_view(['GET'])
def get_Calendrier_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        calandrier = Calandrier.objects.get(pk=pk)
    except Calandrier.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    # Convert the employment data to JSON response
    photocopie_data = {
        'id': str(calandrier.id),
        'Nom': calandrier.Nom,
        'semestre': calandrier.semestre,
        'AU': calandrier.AU,
        'fichier': str(calandrier.fichier)
    }
    
    return JsonResponse(photocopie_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_Calandrier_list(request):
    calandriers = Calandrier.objects.all()
    
    # Convert employments to JSON format
    Calandriers_list = []
    for calandrier in calandriers:
        calandrier_data = {
            'id': str(calandrier.id),
            'Nom': calandrier.Nom,
            'semestre': calandrier.semestre,
            'AU': calandrier.AU,
            'fichier': str(calandrier.fichier)
        }
        Calandriers_list.append(calandrier_data)
    
    return JsonResponse(Calandriers_list, safe=False)



@api_view([ 'PUT'])
def update_Calendrier(request, pk):
    try:
        calandrier = Calandrier.objects.get(pk=pk)
    except Calandrier.DoesNotExist:
        return JsonResponse({"error": "calandrier not found"}, status=404)
    
    if  request.method == 'PUT':
        form = CalandrierForm(request.data, request.FILES)
        if form.is_valid():
            Nom = form.cleaned_data['Nom']
            semestre = form.cleaned_data['semestre']
            AU = form.cleaned_data['AU']
            fichier = form.cleaned_data['fichier']

            calandrier.Nom = Nom
            calandrier.semestre = semestre
            calandrier.AU = AU
            calandrier.fichier = fichier
            calandrier.save()
            
            return JsonResponse({
                'id': str(calandrier.id),
                'Nom': calandrier.Nom,
                'semestre': calandrier.semestre,
                'AU': calandrier.AU,
                'fichier': str(calandrier.fichier)
            })
        return JsonResponse({"error": "photocopie not found"}, status=404)

@api_view(['DELETE'])
def delete_Calendrier(request, pk):
    try:
        calandrier = Calandrier.objects.get(pk=pk)
    except Calandrier.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if request.method == 'DELETE':
        calandrier.delete()
        return JsonResponse({"message": "photocopie deleted successfully"}, status=200)


