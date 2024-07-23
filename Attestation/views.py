from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Serializers import AttestationSerializer
from .models import Attestation



@api_view(['POST'])
def create_Attestation(request):
    if request.method == 'POST':
        attestation_serializer = AttestationSerializer(data=request.data)
        if attestation_serializer.is_valid():
            demande = attestation_serializer.save()
            return Response({"id": str(demande.id), "data": attestation_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(attestation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_Attestation(request, demande_id):
    try:
        demande = Attestation.objects.get(id=demande_id)
    except Attestation.DoesNotExist:
        return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

    demande_data = request.data
    serializer = AttestationSerializer(demande, data=demande_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_attestation_by_cin(request, Cin):
    """
    Récupère tous les demandes ayant le champ Cin égal à la valeur fournie.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des demandes correspondantes et leurs détails.
    """
    try:
        # Recherche des demandes avec le nom du responsable
        mes_attestations = Attestation.objects.filter(Cin=Cin)
        
        if mes_attestations:
            serializer = AttestationSerializer(mes_attestations, many=True)
            
            response_data = []
            
            for data, instance in zip(serializer.data, mes_attestations):
                attestation_data = {
                    "id": str(instance.id),  # Convertir ObjectId en chaîne de caractères
                    "Nom": data['Nom'],
                    "type": data['type'],
                    "idDemande": data['idDemande'],
                    "Cin": data['Cin'],
                    "Etat": data['Etat']
                }
                
                response_data.append(attestation_data)
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "No Demande found for Responsable {}".format(Cin)}, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



   

@api_view(['GET'])
def get_attestation_by_id(request, demande_id):
    """
    Récupère tous les demandes ayant le champ Cin égal à la valeur fournie.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des demandes correspondantes et leurs détails.
    """
    try:
        mes_demande = Attestation.objects.filter(id=demande_id)
        
        if mes_demande:
            serializer = AttestationSerializer(mes_demande, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "No Demande found for id {}".format(demande_id)}, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['DELETE'])
def delete_attestation(request, demande_id):
    try:
        demande = Attestation.objects.get(id=demande_id)
    except Attestation.DoesNotExist:
        return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

    demande.delete()
    return Response({"message": "Demande deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
