from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Type.models import TypeReglement
from .serializers import  TypeReglementSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def add_Type(request):
    if request.method == 'POST':
        regle_serializer = TypeReglementSerializer(data=request.data)
       

        if regle_serializer.is_valid() :
            # Save user
            regle_serializer.save()

            # Save profile
            
            return Response(regle_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def update_type(request, identifiant):
    try:
        reglement = TypeReglement.objects.get(identifiant=identifiant)
    except TypeReglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TypeReglementSerializer(reglement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




   

@api_view(['GET'])
def types(request):
  
    if request.method == 'GET':
        reglements = TypeReglement.objects.all()
        reglementInterieurs = [reglement for reglement in reglements ]
        serializer = TypeReglementSerializer(reglementInterieurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['GET'])
def reglement_by_id(request, name):
    try:
        reglement = TypeReglement.objects.get(name=name)
        serializer = TypeReglementSerializer(reglement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except TypeReglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_reglement(request,name):
    try:
        reglement = TypeReglement.objects.get(name=name)
    except TypeReglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reglement.delete()
        return Response({"message": "Le règlement a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)