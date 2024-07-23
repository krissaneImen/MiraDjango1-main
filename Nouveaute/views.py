from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import NouveauteSerializer
from .models import Nouveaute

@api_view(['POST'])
def create_nouveaute(request):
    serializer = NouveauteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_nouveaute(request, Identifiant):
    try:
        nouveaute = Nouveaute.objects.get(Identifiant=Identifiant)
        serializer = NouveauteSerializer(nouveaute)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Nouveaute.DoesNotExist:
        return Response({"message": "Nouveaute not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_nouveaute(request, Identifiant):
    try:
        nouveaute = Nouveaute.objects.get(Identifiant=Identifiant)
    except Nouveaute.DoesNotExist:
        return Response({"message": "Nouveaute not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = NouveauteSerializer(nouveaute, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_nouveaute(request, Identifiant):
    try:
        nouveaute = Nouveaute.objects.get(Identifiant=Identifiant)
    except Nouveaute.DoesNotExist:
        return Response({"message": "Nouveaute not found"}, status=status.HTTP_404_NOT_FOUND)
    
    nouveaute.delete()
    return Response({"message": "Nouveaute deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def list_nouveautes(request):
    nouveautes = Nouveaute.objects.all()
    serializer = NouveauteSerializer(nouveautes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
