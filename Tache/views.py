from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Tache
from .Serializers import TacheSerializer
from django.http import JsonResponse

@api_view(['POST'])
def create_Tache(request):
    if request.method == 'POST':
        tache_serializer = TacheSerializer(data=request.data)
        if tache_serializer.is_valid():
            tache_serializer.save()
            return Response(tache_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(tache_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_Tache(request, pk):
    try:
        journale = Tache.objects.get(id=pk)
    except Tache.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    groupe_data = request.data
    serializer = TacheSerializer(journale, data=groupe_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_Tache_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            tache = Tache.objects.get(id=groupe_id)
        except Tache.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)
        tache_data = {
                'id': str(tache.id),  # Conversion en chaîne pour l'ID si nécessaire
                'TacheJournaliere': tache.TacheJournaliere,
                'Date': tache.Date,
                
                
                
            }
        serializer = TacheSerializer(tache)
        return Response(tache_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_all_tache(request , id):
    if request.method == 'GET':
        taches = Tache.objects.filter(idJournale=id)
        serialized_journales = []
        for tache in taches:
            tache_data = {
                'id': str(tache.id),  # Conversion en chaîne pour l'ID si nécessaire
                'TacheJournaliere': tache.TacheJournaliere,
                'Date': tache.Date,
                'LastModified': tache.LastModified,
                
                
                
            }
            serialized_journales.append(tache_data)
        return Response(serialized_journales, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['DELETE'])
def delete_Tache(request, pk):
    try:
        actualite = Tache.objects.get(pk=pk)
    except Tache.DoesNotExist:
        return JsonResponse({"error": "Tache not found"}, status=404)
    
    if request.method == 'DELETE':
        actualite.delete()
        return JsonResponse({"message": "Tache deleted successfully"}, status=200)

from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def nombre_taches_par_journale(request , id):
    if request.method == 'GET':
        taches = Tache.objects.filter(idJournale=id)
        nombre_de_taches = taches.count()  # Compter le nombre total de tâches
        serialized_journales = []
        tache_data = {
                'nombre_de_taches': nombre_de_taches,
                
            }
        serialized_journales.append(tache_data)
        
        # Retourner à la fois les données sérialisées et le nombre total de tâches
        return Response(serialized_journales, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



