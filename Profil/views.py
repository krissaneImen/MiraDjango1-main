# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Profil.serializers import ProfileSerializer
from .serializiers import  ProfileSignUpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Profil


import base64

@api_view(['POST'])
def Create_profile(request):
    if request.method == 'POST':
        profile_serializer = ProfileSignUpSerializer(data=request.data)
        if profile_serializer.is_valid() :
            # Save user
            profile_serializer.save()

            # Save profile
            
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def update_profile(request, cin):
    try:
        profile = Profil.objects.get(cartCin=cin)
    except Profil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    profile_data = request.data
    # Assuming image data is sent as base64 string in request.data
    
    
    serializer = ProfileSerializer(profile, data=profile_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_profile_by_cin(request, cin):
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
        profiles = Profil.objects.filter(cartCin=cin)
        
        # Check if any profile exists
        if profiles:
            # Assuming CIN is unique, we take the first profile found
            profile = profiles.first()
            
            # Serialize the profile data
            serializer = ProfileSignUpSerializer(profile)

            # Convert image data to base64 string
            
            # Include image base64 string in the serialized data
            serialized_data = serializer.data
            
            return Response(serialized_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_profile(request, cin):
    """
    Supprime un profil utilisateur.

    Paramètres :
    - request : HttpRequest - la requête HTTP.
    - cin : str - le CIN du profil à supprimer.

    Retour :
    - Response : réponse HTTP avec le statut approprié et un message indiquant si la suppression a réussi ou non.
    """
    try:
        profile = Profil.objects.get(cartCin=cin)
    except Profil.DoesNotExist:
        return Response({"message": "Profil non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        profile.delete()
        return Response({"message": "Profil supprimé avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
