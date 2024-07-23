from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Manifestation
from .serializers import ManifestationSerializer
from datetime import datetime
from mongoengine.queryset.visitor import Q

@api_view(['POST'])
def create_manifestation(request):
    if request.method == 'POST':
        serializer = ManifestationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_manifestation(request, Identifiant):
    try:
        manifestation = Manifestation.objects.get(Identifiant=Identifiant)
    except Manifestation.DoesNotExist:
        return Response({"message": "Manifestation not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ManifestationSerializer(manifestation, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_manifestation_by_id(request, Identifiant):
    try:
        manifestation = Manifestation.objects.get(Identifiant=Identifiant)
    except Manifestation.DoesNotExist:
        return Response({"message": "Manifestation not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ManifestationSerializer(manifestation)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_manifestations(request):
    manifestations = Manifestation.objects.all()
    serializer = ManifestationSerializer(manifestations, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_manifestations_by_userType(request , userType):
    """
    Get all formations.

    Parameters:
    - request: HttpRequest - the HTTP request.

    Returns:
    - Response: JSON response with all formations data.
    """
    if request.method == 'GET':

        userType = userType.lower()
        manifestations = Manifestation.objects.filter()
        if (userType=='etudiant'):
            ManifestationCible = [manifestation for manifestation in manifestations if  manifestation.etudiant]
        elif (userType=='enseignant'):
            ManifestationCible = [manifestation for manifestation in manifestations if  manifestation.enseignant]
        elif (userType=='administratif'):
            ManifestationCible = [manifestation for manifestation in manifestations if  manifestation.administratif]
        else :
            ManifestationCible = [manifestation for manifestation in manifestations if  manifestation.administrateur]


        
        serializer = ManifestationSerializer(ManifestationCible, many=True)
        
        # Convert image data to base64 string (if needed)
        
        # Include image base64 string in the serialized data (if needed)
        serialized_data = serializer.data
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_manifestation(request, Identifiant):
    try:
        manifestation = Manifestation.objects.get(Identifiant=Identifiant)
    except Manifestation.DoesNotExist:
        return Response({"message": "Manifestation not found"}, status=status.HTTP_404_NOT_FOUND)

    manifestation.delete()
    return Response({"message": "Manifestation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_manifestations_by_date(request, userType, date_min, date_max):
    try:
        date_min_obj = datetime.strptime(date_min, '%Y-%m-%d').date()
        date_max_obj = datetime.strptime(date_max, '%Y-%m-%d').date()
    except ValueError:
        return Response({"message": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)


    userType = userType.lower()
    if userType == 'etudiant':
        manifestations = Manifestation.objects.filter(Q(etudiant__exists=True) & Q(dateDebut__gte=date_min_obj) & Q(dateDebut__lte=date_max_obj))
    elif userType == 'enseignant':
        manifestations = Manifestation.objects.filter(Q(enseignant__exists=True) & Q(dateDebut__gte=date_min_obj) & Q(dateDebut__lte=date_max_obj))
    elif userType == 'administratif':
        manifestations = Manifestation.objects.filter(Q(administratif__exists=True) & Q(dateDebut__gte=date_min_obj) & Q(dateDebut__lte=date_max_obj))
    elif userType == 'administrateur':
        manifestations = Manifestation.objects.filter(Q(administrateur__exists=True) & Q(dateDebut__gte=date_min_obj) & Q(dateDebut__lte=date_max_obj))
    else:
        return Response({"message": "Invalid userType"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ManifestationSerializer(manifestations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
