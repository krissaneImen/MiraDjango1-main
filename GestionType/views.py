from django.http import JsonResponse
from django.shortcuts import render
from .forms import TypeGlogableForm
from .models import TypeGlogable
from rest_framework.decorators import api_view
from django.http import HttpResponse, Http404
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status


from django.http import JsonResponse
from rest_framework.decorators import api_view
from .forms import TypeGlogableForm  # Assurez-vous d'importer le formulaire correctement
from .models import TypeGlogable

@api_view(['POST'])
def create_type(request):
    if request.method == 'POST':
        form = TypeGlogableForm(request.POST, request.FILES)
        if form.is_valid():
            # Extracting data from the form
            name = form.cleaned_data['name']
            fonctionalite = form.cleaned_data['fonctionalite']
            etudiant = form.cleaned_data['etudiant']
            enseignant = form.cleaned_data['enseignant']
            administratif = form.cleaned_data['administratif']
            administrateur = form.cleaned_data['administrateur']
            
            # Saving the TypeGlogable object
            typeglobal = TypeGlogable(
                name=name,
                fonctionalite=fonctionalite,
                etudiant=etudiant,
                enseignant=enseignant,
                administratif=administratif,
                administrateur=administrateur,
            )
            typeglobal.save()
            
            # Returning the newly created TypeGlogable object data in JSON response
            return JsonResponse({
                'id': str(typeglobal.id),  # Convert ObjectId to string
                'name': typeglobal.name,
                'fonctionalite': typeglobal.fonctionalite,
                'etudiant': typeglobal.etudiant,
                'enseignant': typeglobal.enseignant,
                'administratif': typeglobal.administratif,
                'administrateur': typeglobal.administrateur,
            })
        else:
            # Return form errors in JSON response
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        # Return method not allowed error
        return JsonResponse({'error': 'Méthode non autorisée'}, status=405)


@api_view(['GET'])
def get_type_by_id(request, pk):
    try:
        # Retrieve the ClassSchedule object by its primary key (pk)
        typeglobal = TypeGlogable.objects.get(pk=pk)
    except TypeGlogable.DoesNotExist:
        # If the object is not found, return an appropriate response
        return JsonResponse({"error": "actualite not found"}, status=404)
    
    # Convert the employment data to JSON response
    actualite_data = {
        'id': str(typeglobal.id),
        'name': typeglobal.name,
        'fonctionalite': typeglobal.fonctionalite,
        'etudiant': typeglobal.etudiant,
        'enseignant': typeglobal.enseignant,
        'administratif': typeglobal.administratif,
        'administrateur': typeglobal.administrateur,
          }
    
    return JsonResponse(actualite_data)


# Django View for retrieving the list of employments
@api_view(['GET'])
def get_type_list(request):
    types = TypeGlogable.objects.all()
    
    # Convert employments to JSON format
    type_list = []
    for actualite in types:
        actualite_data = {
            'id': str(actualite.id),
            'name': actualite.name,
            'fonctionalite': actualite.fonctionalite,
            'etudiant': actualite.etudiant,
            'enseignant': actualite.enseignant,
            'administratif': actualite.administratif,
            'administrateur': actualite.administrateur,
            }
        type_list.append(actualite_data)
    
    return JsonResponse(type_list, safe=False)





@api_view(['PUT'])
def update_type(request, pk):
    try:
        typeglobal = TypeGlogable.objects.get(pk=pk)
    except TypeGlogable.DoesNotExist:
        return JsonResponse({"error": "Actualite not found"}, status=404)
    
    if request.method == 'PUT':
        form = TypeGlogableForm(request.data, request.FILES)
        if form.is_valid():
            typeglobal.name = form.cleaned_data['name']
            typeglobal.fonctionalite = form.cleaned_data['fonctionalite']
            typeglobal.etudiant = form.cleaned_data['etudiant']
            typeglobal.enseignant = form.cleaned_data['enseignant']
            typeglobal.administratif = form.cleaned_data['administratif']
            typeglobal.administrateur = form.cleaned_data['administrateur']
           
            typeglobal.save()

            return JsonResponse({
                'id': str(typeglobal.id),
                'name': typeglobal.name,
                'fonctionalite': typeglobal.fonctionalite,
                'etudiant': typeglobal.etudiant,
                'enseignant': typeglobal.enseignant,
                'administratif': typeglobal.administratif,
                'administrateur': typeglobal.administrateur,
                  })
        else:
            return JsonResponse(form.errors, status=400)  # Return form errors if form is invalid
    else:
        return JsonResponse({"error": "PUT method required"}, status=405)  # Return method not allowed error for non-PUT requests
    

@api_view(['DELETE'])
def delete_type(request, pk):
    try:
        typeglobale = TypeGlogable.objects.get(pk=pk)
    except TypeGlogable.DoesNotExist:
        return JsonResponse({"error": "photocopie not found"}, status=404)
    
    if request.method == 'DELETE':
        typeglobale.delete()
        return JsonResponse({"message": "actualite deleted successfully"}, status=200)




@api_view(['GET'])
def get_all_type(request, userType):
    
    if request.method == 'GET':
        # Filter actualites based on userType
        if userType == 'etudiant':
            types = TypeGlogable.objects.filter(etudiant=True)
        elif userType == 'enseignant':
            types = TypeGlogable.objects.filter(enseignant=True)
        elif userType == 'administratif':
            types = TypeGlogable.objects.filter(administratif=True)
        elif userType == 'administrateur':
            types = TypeGlogable.objects.filter(administrateur=True)
        else:
            return Response({"error": "Invalid userType"}, status=status.HTTP_400_BAD_REQUEST)

        # Manually construct serialized data from queryset
        type_list = []
        for type in types:
            type_data = {
                'id': str(type.id),
                'fonctionalite': type.fonctionalite,
                'name': type.name,
                'etudiant': type.etudiant,
                'enseignant': type.enseignant,
                'administratif': type.administratif,
                'administrateur': type.administrateur,
                }
            type_list.append(type_data)

        return Response(type_list, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_types_by_user_type_and_functionality(request, userType, fonctionalite):
    
    if request.method == 'GET':
        # Filtrer les types en fonction du type d'utilisateur et de la fonctionnalité
        if userType == 'etudiant':
            types = TypeGlogable.objects.filter(etudiant=True, fonctionalite=fonctionalite)
        elif userType == 'enseignant':
            types = TypeGlogable.objects.filter(enseignant=True, fonctionalite=fonctionalite)
        elif userType == 'administratif':
            types = TypeGlogable.objects.filter(administratif=True, fonctionalite=fonctionalite)
        elif userType == 'administrateur':
            types = TypeGlogable.objects.filter(administrateur=True, fonctionalite=fonctionalite)
        else:
            return Response({"error": "Type d'utilisateur invalide"}, status=status.HTTP_400_BAD_REQUEST)

        # Construire manuellement les données sérialisées à partir de la queryset
        type_list = []
        for type in types:
            type_data = {
                'id': str(type.id),
                'fonctionalite': type.fonctionalite,
                'name': type.name,
                'etudiant': type.etudiant,
                'enseignant': type.enseignant,
                'administratif': type.administratif,
                'administrateur': type.administrateur,
                }
            type_list.append(type_data)

        return Response(type_list, status=status.HTTP_200_OK)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
