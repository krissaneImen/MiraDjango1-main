from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Institut
from .serializers import InstitutSerializer



@api_view(['POST'])
def create_Institut(request):
    if request.method == 'POST':
        institut_serializer = InstitutSerializer(data=request.data)
        if institut_serializer.is_valid():
            institut_serializer.save()
            return Response(institut_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(institut_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_institut(request, institut_id):
    try:
        institut = Institut.objects.get(id=institut_id)
    except Institut.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    institut_data = request.data
    serializer = InstitutSerializer(institut, data=institut_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_Institut(request):
    if request.method == 'GET':
        try:
            # Query all instances of Institut
            instituts = Institut.objects.all()
            
            if instituts:
                # Serialize the data
                serializer = InstitutSerializer(instituts, many=True)
                
                # Build a list of dictionaries with the ID and other serialized data fields
                instituts_data = [{'id': str(institut.id), **serializer.data[i]} for i, institut in enumerate(instituts)]
                
                return Response(instituts_data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Aucun institut trouvé"}, status=status.HTTP_404_NOT_FOUND)
        except Institut.DoesNotExist:
            return Response({"message": "Institut non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
