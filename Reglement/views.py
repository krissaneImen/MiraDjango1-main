from django.http import JsonResponse
from django.shortcuts import render
from .forms import ReglementForm
from .models import ReglementPdf
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.core.files.base import ContentFile
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
def create_reglement(request):
    if request.method == 'POST':
        form = ReglementForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            type = form.cleaned_data['type']
            etudiant = form.cleaned_data['etudiant']
            enseignant = form.cleaned_data['enseignant']
            administratif = form.cleaned_data['administratif']
            administrateur = form.cleaned_data['administrateur']
            pdf_file = form.cleaned_data['pdf_file']
            
            # Saving uploaded file to the database
            reglement = ReglementPdf(
                name=name,
                description=description,
                type=type,
                etudiant=etudiant,
                enseignant=enseignant,
                administratif=administratif,
                administrateur=administrateur,
                pdf_file=pdf_file
            )
            reglement.save()
            
            # Returning uploaded file data in JSON response
            return JsonResponse({
                'id': str(reglement.id),  # Convert ObjectId to string
                'name': reglement.name,
                'description': reglement.description,
                'type': reglement.type,
                'etudiant': reglement.etudiant,
                'enseignant': reglement.enseignant,
                'administratif': reglement.administratif,
                'administrateur': reglement.administrateur,
                'pdf_file': str(reglement.pdf_file)  # Convert GridFSProxy to string
            })
    else:
        form = ReglementForm()
    return JsonResponse({
                  # Convert GridFSProxy to string
})

def open_pdf(request, pk):
    try:
        reglement = ReglementPdf.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return HttpResponse("Photocopie not found", status=404)
    
    # Assuming fichier is the field that stores the PDF file
    pdf_file = reglement.pdf_file
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set inline header to display PDF in browser
    response['Content-Disposition'] = 'inline; filename="%s"' % reglement.pdf_file.name
    
    return response



def download_pdf(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        reglement = ReglementPdf.objects.get(pk=pk)
    except ReglementPdf.DoesNotExist:
        # If the object is not found, return an appropriate response
        return HttpResponse("reglement not found", status=404)
    
    # Assuming emploiFile is the field that stores the PDF file
    pdf_file = reglement.pdf_file
    
    # Set content type as PDF
    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
    
    # Set attachment header to force download
    response['Content-Disposition'] = 'inline; filename="%s"' % reglement.pdf_file.name
    
    return response

@api_view(['GET'])
def get_Reglement_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        reglement = ReglementPdf.objects.get(pk=pk)
    except ReglementPdf.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "reglement not found"}, status=404)
    
    # Convert the employment data to JSON response
    reglement_data = {
        'id': str(reglement.id),
        'name': reglement.name,
        'type': reglement.type,
        'description': reglement.description,
        'etudiant': reglement.etudiant,
        'enseignant': reglement.enseignant,
        'administratif': reglement.administratif,
        'administrateur': reglement.administrateur,
        'pdf_file': str(reglement.pdf_file) 
    }
    
    return JsonResponse(reglement_data)

@api_view(['GET'])
def get_reglement_list(request):
    reglements = ReglementPdf.objects.all()
    
    # Convert employments to JSON format
    reglement_list = []
    for reglement in reglements:
        reglement_data = {
            'id': str(reglement.id),
            'name': reglement.name,
            'type': reglement.type,
            'description': reglement.description,
            'etudiant': reglement.etudiant,
            'enseignant': reglement.enseignant,
            'administratif': reglement.administratif,
            'administrateur': reglement.administrateur,
            'pdf_file': str(reglement.pdf_file) 
        }
        reglement_list.append(reglement_data)
    
    return JsonResponse(reglement_list, safe=False)


@api_view([ 'PUT'])
def update_reglement(request, pk):
    try:
        calandrier = ReglementPdf.objects.get(pk=pk)
    except ReglementPdf.DoesNotExist:
        return JsonResponse({"error": "reglement  not found"}, status=404)
    
    if  request.method == 'PUT':
        form = ReglementForm(request.data, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            type = form.cleaned_data['type']
            etudiant = form.cleaned_data['etudiant']
            enseignant = form.cleaned_data['enseignant']
            administratif = form.cleaned_data['administratif']
            administrateur = form.cleaned_data['administrateur']
            pdf_file = form.cleaned_data['pdf_file']

            calandrier.name = name
            calandrier.description = description
            calandrier.type = type
            calandrier.etudiant = etudiant
            calandrier.enseignant = enseignant
            calandrier.administratif = administratif
            calandrier.administrateur = administrateur
            calandrier.pdf_file = pdf_file
            calandrier.save()
            
            return JsonResponse({
                'id': str(calandrier.id),
                'name': calandrier.name,
                'description': calandrier.description,
                'type': calandrier.type,
                'etudiant': calandrier.etudiant,
                'enseignant': calandrier.enseignant,
                'administratif': calandrier.administratif,
                'administrateur': calandrier.administrateur,
                'pdf_file': str(calandrier.pdf_file)
            })
        return JsonResponse({"error": "photocopie not found"}, status=404)



@api_view(['DELETE'])
def delete_reglement(request, pk):
    try:
        reglement = ReglementPdf.objects.get(pk=pk)
    except ReglementPdf.DoesNotExist:
        return JsonResponse({"error": "reglement not found"}, status=404)
    
    if request.method == 'DELETE':
        reglement.delete()
        return JsonResponse({"message": "reglement deleted successfully"}, status=200)

@api_view(['GET'])
def get_reglement_by_type(request, reglement_type):
    try:
        # Retrieve the ClassSchedule objects filtered by type
        reglements = ReglementPdf.objects.filter(type=reglement_type)
    except ReglementPdf.DoesNotExist:
        # If no objects are found, return an appropriate response
        return JsonResponse({"error": "Employment not found"}, status=404)
    
    # Convert the employments data to a list of JSON responses
    reglement_list = []
    for reglement in reglements:
        reglement_data = {
            'id': str(reglement.id),
            'name': reglement.name,
            'type': reglement.type,
            'description': reglement.description,
            'etudiant': reglement.etudiant,
            'enseignant': reglement.enseignant,
            'administratif': reglement.administratif,
            'administrateur': reglement.administrateur,
            'pdf_file': str(reglement.pdf_file)  # Convert GridFSProxy to string
            
        }
        reglement_list.append(reglement_data)
    
    return JsonResponse(reglement_list, safe=False)


