from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Avis
from .Serializers import AvisSerializer

@api_view(['POST'])
def create_Avis(request):
    if request.method == 'POST':
        avis_serializer = AvisSerializer(data=request.data)
        if avis_serializer.is_valid():
            avis_serializer.save()
            return Response(avis_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(avis_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['PUT'])
def update_avis(request, groupe_id):
    try:
        avis = Avis.objects.get(id=groupe_id)
    except Avis.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    avis_data = request.data
    serializer = AvisSerializer(avis, data=avis_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_avis_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            avis = Avis.objects.get(id=groupe_id)
        except Avis.DoesNotExist:
            return Response({"message": "avis not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AvisSerializer(avis)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





@api_view(['GET'])
def get_all_avis(request):
    if request.method == 'GET':
        avise = Avis.objects.all()
        serialized_avis = []
        for avis in avise:
            avis_data = {
                'id': str(avis.id),  # Conversion en chaîne pour l'ID si nécessaire
                'type': avis.type,
                'etat': avis.etat,
                'enseignant': avis.enseignant,
                'cinEnseignant': avis.cinEnseignant,
                'heureDebut': avis.heureDebut,
                'heureFin': avis.heureFin,
                'DateAvis': avis.DateAvis,
                'Datefin': avis.Datefin,
                'Anneeuniversitaire': avis.Anneeuniversitaire,
                'Classes': avis.Classes,
            }
            serialized_avis.append(avis_data)
        return Response(serialized_avis, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_avis_by_group(request, NomGroupe):
    if request.method == 'GET':
        avis = Avis.objects.filter(Classes__contains=NomGroupe)
        serialized_avis = AvisSerializer(avis, many=True)
        return Response(serialized_avis.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def get_avis_by_state(request, state):
    if request.method == 'GET':
        avis = Avis.objects.filter(etat=state)
        serialized_avis = AvisSerializer(avis, many=True)
        return Response(serialized_avis.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_avis_by_state_and_group(request, state, group_id):
    if request.method == 'GET':
        avis = Avis.objects.filter(etat=state, Classes__contains=group_id)
        serialized_avis = AvisSerializer(avis, many=True)
        return Response(serialized_avis.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_avis_by_cin(request, cin):
    if request.method == 'GET':
        avis = Avis.objects.filter(cinEnseignant=cin)
        serialized_avis = AvisSerializer(avis, many=True)
        return Response(serialized_avis.data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
