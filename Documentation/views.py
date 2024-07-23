from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReglementSerializer
from .models import Reglement
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['POST'])
def add_rule(request):
    if request.method == 'POST':
        regle_serializer = ReglementSerializer(data=request.data)
       

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




""" 
@api_view(['POST'])
def add_rule(request):
    if request.method == 'POST':
        identifiant = request.data.get('identifiant')
        titre = request.data.get('titre')
        description = request.data.get('description')
        type = request.data.get('type')
        pdf_file = request.FILES.get('pdf_file')

        if not identifiant or not titre or not type or not pdf_file:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

        new_pdf_file = ReglementSerializer(identifiant=identifiant, titre=titre , description = description ,type =type , pdf_file=pdf_file)
        new_pdf_file.save()

        serialized_data = ReglementSerializer(new_pdf_file).data

        return Response(serialized_data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

 """

@api_view(['PUT'])
def update_reglement(request, identifiant):
    try:
        reglement = Reglement.objects.get(identifiant=identifiant)
    except Reglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ReglementSerializer(reglement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def reglement_interieur(request):
  
    if request.method == 'GET':
        reglements = Reglement.objects.all()
        reglementInterieurs = [reglement for reglement in reglements if reglement.type == "interieur"]
        serializer = ReglementSerializer(reglementInterieurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def reglement_examens(request):
  
    if request.method == 'GET':
        reglements = Reglement.objects.all()
        reglementInterieurs = [reglement for reglement in reglements if reglement.type == "examens"]
        serializer = ReglementSerializer(reglementInterieurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def reglements(request):
  
    if request.method == 'GET':
        reglements = Reglement.objects.all()
        reglementInterieurs = [reglement for reglement in reglements ]
        serializer = ReglementSerializer(reglementInterieurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def reglement_by_type(request , reglement_type):
  
    if request.method == 'GET':
        reglements = Reglement.objects.all()
        reglementInterieurs = [reglement for reglement in reglements if reglement.type == reglement_type]
        serializer = ReglementSerializer(reglementInterieurs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




@api_view(['GET'])
def reglement_by_id(request, identifiant):
    try:
        reglement = Reglement.objects.get(identifiant=identifiant)
        serializer = ReglementSerializer(reglement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Reglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def reglements_by_usertype(request, userType):
    """
    Get all reglements filtered by userType.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - userType: str - the type of user (e.g., 'etudiant', 'enseignant', 'administratif', 'administrateur').

    Returns:
    - Response: JSON response with filtered reglements data.
    """
    if request.method == 'GET':
        # Query all reglements
        reglements = Reglement.objects.all()
        
        # Filter reglements based on userType
        if userType == 'etudiant':
            reglements_filtered = [reglement for reglement in reglements if reglement.etudiant]
        elif userType == 'enseignant':
            reglements_filtered = [reglement for reglement in reglements if reglement.enseignant]
        elif userType == 'administratif':
            reglements_filtered = [reglement for reglement in reglements if reglement.administratif]
        else:
            reglements_filtered = [reglement for reglement in reglements if reglement.administrateur]

        # Serialize the filtered reglements
        serializer = ReglementSerializer(reglements_filtered, many=True)
        serialized_data = serializer.data
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_reglement(request, identifiant):
    try:
        reglement = Reglement.objects.get(identifiant=identifiant)
    except Reglement.DoesNotExist:
        return Response({"message": "Le règlement n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        reglement.delete()
        return Response({"message": "Le règlement a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)

    return Response({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)