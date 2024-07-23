from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from User.models import User
from .serializers import DemandeSerializer
from .models import Demande

@api_view(['POST'])
def create_demande(request):
    if request.method == 'POST':
        demande_serializer = DemandeSerializer(data=request.data)
        if demande_serializer.is_valid():
            demande = demande_serializer.save()
            # Retourner tous les champs du modèle dans la réponse
            return Response({
                "id": str(demande.id),
                "Demande": demande.Demande,
                "Responsable": demande.Responsable,
                "Cin": demande.Cin,
                "DateDemande": demande.DateDemande,
                "PretLe": demande.PretLe,
                "Etat": demande.Etat,
                "data": demande_serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(demande_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['PUT'])
def update_demande(request, demande_id):
    try:
        demande = Demande.objects.get(id=demande_id)
    except Demande.DoesNotExist:
        return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

    demande_data = request.data
    serializer = DemandeSerializer(demande, data=demande_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_demande_by_cin(request, Cin):
    """
    Récupère tous les demandes ayant le champ Cin égal à la valeur fournie.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des demandes correspondantes et leurs détails.
    """
    try:
        mes_demande = Demande.objects.filter(Cin=Cin)
        
        if mes_demande:
            serializer = DemandeSerializer(mes_demande, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "No Demande found for Cin {}".format(Cin)}, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_demande_by_id(request, demande_id):
    """
    Récupère la demande ayant l'ID égal à la valeur fournie.

    Retour :
    - HttpResponse : réponse HTTP avec l'ID de la demande et ses détails.
    """
    try:
        demande = Demande.objects.get(id=demande_id)
        
        serializer = DemandeSerializer(demande)
        
        response_data = {
            "id": demande_id,
            "Demande": serializer.data['Demande'],
            "Responsable": serializer.data['Responsable'],
            "Cin": serializer.data['Cin'],
            "DateDemande": serializer.data['DateDemande'],
            "PretLe": serializer.data['PretLe'],
            "Etat": serializer.data['Etat']
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
            
    except Demande.DoesNotExist:
        return Response({"message": "No Demande found for id {}".format(demande_id)}, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['DELETE'])
def delete_demande(request, demande_id):
    try:
        demande = Demande.objects.get(id=demande_id)
    except Demande.DoesNotExist:
        return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

    demande.delete()
    return Response({"message": "Demande deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def get_demande_by_responsable(request, responsable_name):
    """
    Récupère toutes les demandes ayant le nom du responsable égal à la valeur fournie.

    Retour :
    - HttpResponse : réponse HTTP avec les détails des demandes.
    """
    try:
        # Recherche des demandes avec le nom du responsable
        mes_demandes = Demande.objects.filter(Responsable=responsable_name)
        
        if mes_demandes:
            serializer = DemandeSerializer(mes_demandes, many=True)
            
            response_data = []
            
            for data, instance in zip(serializer.data, mes_demandes):
                demande_data = {
                    "id": str(instance.id),  # Convertir ObjectId en chaîne de caractères
                    "Demande": data['Demande'],
                    "Responsable": data['Responsable'],
                    "Cin": data['Cin'],
                    "DateDemande": data['DateDemande'],
                    "PretLe": data['PretLe'],
                    "Etat": data['Etat']
                }
                
                response_data.append(demande_data)
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message": "No Demande found for Responsable {}".format(responsable_name)}, status=status.HTTP_404_NOT_FOUND)
            
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_demande_etat(request, demande_id, etat):
    """
    Met à jour l'attribut 'Etat' d'une demande spécifique et envoie un e-mail pour informer l'utilisateur de la mise à jour.

    Arguments :
    - demande_id : ID de la demande à mettre à jour.
    - etat : Nouvel état à assigner à la demande.

    Retour :
    - HttpResponse : réponse HTTP avec les détails de la demande mise à jour.
    """
    
    # Liste des états valides
    etats_valides = ['En attente', 'En cours de traitement', 'Rejeté', 'Terminé']

    try:
        demande = Demande.objects.get(id=demande_id)
    except Demande.DoesNotExist:
        return Response({"message": "Demande not found"}, status=status.HTTP_404_NOT_FOUND)

    # Vérification si l'état est valide
    if etat in etats_valides:
        demande.Etat = etat
    else:
        return Response({"message": f"'{etat}' is not a valid state"}, status=status.HTTP_400_BAD_REQUEST)

    serializer = DemandeSerializer(demande, data={'Etat': demande.Etat}, partial=True)
    if serializer.is_valid():
        # Enregistrer la demande mise à jour
        serializer.save()

        # Récupérer l'email de l'utilisateur par CIN
        user_cin = demande.Cin
        try:
            user = User.objects.get(cin=user_cin)
            user_email = user.email
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Envoyer un e-mail à l'utilisateur
        subject = 'Mise à jour de l\'état de votre demande'
        message = f'L\'état de votre demande a été mis à jour. Nouvel état : {etat}'
        from_email = 'adminmira@coursenligne.info',  # Remplacez par votre adresse e-mail
        to_email = [user_email]
        print(to_email)
        send_mail(
            'Mise à jour de l\'état de votre demande',
            f'L\'état de votre  {demande.Demande} a été mis à jour. Nouvel état : {etat}',
            'adminmira@coursenligne.info',
            to_email,
            fail_silently=False,
        )

        # Retourner les détails de la demande mise à jour
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
