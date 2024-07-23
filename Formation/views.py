# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from mongoengine.queryset.visitor import Q
from Formation.serializers import FormationSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Formation
from datetime import datetime


import base64

@api_view(['POST'])
def Create_Formation(request):
    if request.method == 'POST':
        formation_serializer = FormationSerializer(data=request.data)
        if formation_serializer.is_valid() :
            # Save user
            formation_serializer.save()

            # Save profile
            
            return Response(formation_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def update_formation(request, Identifiant):
    try:
        formation = Formation.objects.get(Identifiant=Identifiant)
    except Formation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    formation_data = request.data
    # Assuming image data is sent as base64 string in request.data
    
    
    serializer = FormationSerializer(formation, data=formation_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_formation_by_cin(request, Identifiant):
    """
    Get a user's profile by their CIN.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - cin: str - the CIN of the user to retrieve.

    Returns:
    - Response: JSON response with the user's profile data or an error message if not found.
    """
    if request.method == 'GET':
        # Query the profile by CIN
        formations = Formation.objects.filter(Identifiant=Identifiant)
        
        # Check if any profile exists
        if formations:
            # Assuming CIN is unique, we take the first profile found
            formation = formations.first()
            
            # Serialize the profile data
            serializer = FormationSerializer(formation)

            serialized_data = serializer.data
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_all_formations(request , userType):
    """
    Get all formations.

    Parameters:
    - request: HttpRequest - the HTTP request.

    Returns:
    - Response: JSON response with all formations data.
    """
    if request.method == 'GET':
        # Query all formations
        formations = Formation.objects.filter()
        userType = userType.lower()
        if (userType=='etudiant'):
            FormationCible = [formation for formation in formations if  formation.etudiant]
        elif (userType=='enseignant'):
            FormationCible = [formation for formation in formations if  formation.enseignant]
        elif (userType=='administratif'):
            FormationCible = [formation for formation in formations if  formation.administratif]
        else :
            FormationCible = [formation for formation in formations if  formation.administrateur]


        
        serializer = FormationSerializer(FormationCible, many=True)
        
        # Convert image data to base64 string (if needed)
        
        # Include image base64 string in the serialized data (if needed)
        serialized_data = serializer.data
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_formations(request ):
    
    if request.method == 'GET':
        # Query all formations
        formations = Formation.objects.filter()
        
        serializer = FormationSerializer(formations, many=True)
        serialized_data = serializer.data
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_formation(request, Identifiant):
    """
    Delete a formation by its identifier.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - Identifiant: str - the identifier of the formation to delete.

    Returns:
    - Response: JSON response indicating success or failure of the deletion operation.
    """
    try:
        # Get the formation object by its identifier
        formation = Formation.objects.get(Identifiant=Identifiant)
    except Formation.DoesNotExist:
        # If formation does not exist, return 404 NOT FOUND
        return Response({"message": "Formation not found"}, status=status.HTTP_404_NOT_FOUND)

    # Delete the formation
    formation.delete()

    # Return success message
    return Response({"message": "Formation deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_formations_by_date(request, userType, date_min, date_max):
    try:
        date_min_obj = datetime.strptime(date_min, '%Y-%m-%d').date()
        date_max_obj = datetime.strptime(date_max, '%Y-%m-%d').date()
    except ValueError:
        return Response({"message": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

    if userType == 'etudiant':
        formations = Formation.objects.filter(Q(etudiant__exists=True) & Q(dateDeFormation__gte=date_min_obj) & Q(dateDeFormation__lte=date_max_obj))
    elif userType == 'enseignant':
        formations = Formation.objects.filter(Q(enseignant__exists=True) & Q(dateDeFormation__gte=date_min_obj) & Q(dateDeFormation__lte=date_max_obj))
    elif userType == 'administratif':
        formations = Formation.objects.filter(Q(administratif__exists=True) & Q(dateDeFormation__gte=date_min_obj) & Q(dateDeFormation__lte=date_max_obj))
    elif userType == 'administrateur':
        formations = Formation.objects.filter(Q(administrateur__exists=True) & Q(dateDeFormation__gte=date_min_obj) & Q(dateDeFormation__lte=date_max_obj))
    else:
        return Response({"message": "Invalid userType"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = FormationSerializer(formations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)




