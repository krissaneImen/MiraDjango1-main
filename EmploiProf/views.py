
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EmploiProf
from .Serializers import EmploiSerializer

@api_view(['POST'])
def create_emploi(request):
    if request.method == 'POST':
        emploi_serializer = EmploiSerializer(data=request.data)
        if emploi_serializer.is_valid():
            emploi_serializer.save()
            return Response(emploi_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(emploi_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_emploi(request, groupe_id):
    try:
        seance = EmploiProf.objects.get(id=groupe_id)
    except EmploiProf.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    groupe_data = request.data
    serializer = EmploiSerializer(seance, data=groupe_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_emploi_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            seance = EmploiProf.objects.get(id=groupe_id)
        except EmploiProf.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmploiSerializer(seance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['GET'])
def get_emploi_by_cin(request, cin):
    if request.method == 'GET':
        try:
            emploi = EmploiProf.objects.get(CinEnseignant=cin)
        except EmploiProf.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmploiSerializer(emploi)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_all_seances(request):
    if request.method == 'GET':
        seances = EmploiProf.objects.all()
        serialized_seances = []
        for seance in seances:
            seance_data = seance.to_dict()
            seance_data['Seances'] = [seance.to_dict() for seance in seance.Seances]
            serialized_seances.append(seance_data)
        return Response(serialized_seances, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

from .models import EmploiProf

@api_view(['GET'])
def get_seance_par_horaire_jourSemaine(request, horaire, jourSemaine):
    if request.method == 'GET':
        try:
            # Recherchez parmi toutes les séances pour trouver la séance avec le bon horaire et jour de la semaine
            emploi_prof = EmploiProf.objects.filter(Seances__horaire=horaire, Seances__jourSemaine=jourSemaine).first()

            if emploi_prof:
                # Si une séance est trouvée, retournez-la
                seance = emploi_prof.get_Seance(horaire, jourSemaine)
                if seance:
                    return Response({"seance": seance.to_dict()}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Seance not found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                # Sinon, retournez un message indiquant que la séance n'a pas été trouvée
                return Response({"message": "EmploiProf not found"}, status=status.HTTP_404_NOT_FOUND)
        except :
            # Si l'emploi professionnel n'est pas trouvé, retournez un message indiquant qu'il n'a pas été trouvé
            return Response({"message": "EmploiProf not found"}, status=status.HTTP_404_NOT_FOUND)

    # Si la méthode HTTP n'est pas GET, retournez un message indiquant que la méthode n'est pas autorisée
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_seances_by_emploi(request, groupe_id):
    if request.method == 'GET':
        try:
            # Récupérer le groupe spécifié par l'identifiant
            emploi = EmploiProf.objects.get(id=groupe_id)
        except EmploiProf.DoesNotExist:
            return Response({"message": "emploi not found"}, status=status.HTTP_404_NOT_FOUND)

        # Liste des étudiants du groupe
        seances_list = []

        # Parcourir chaque étudiant dans le groupe
        for seance in emploi.Seances:
            seance_data = {
                'horaire': seance.horaire,
                'matiere': seance.matiere,
                'sale': seance.sale,
                'jourSemaine': seance.jourSemaine,
                'groupe': seance.groupe,
                }
            seances_list.append(seance_data)

        return Response(seances_list, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['DELETE'])
def delete_emploi(request, groupe_id):
    try:
        # Recherchez le groupe par son identifiant
        emploi = EmploiProf.objects.get(id=groupe_id)
    except EmploiProf.DoesNotExist:
        return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

    # Suppression du groupe
    emploi.delete()
    return Response({"message": "Groupe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def get_seances_by_cin(request, cin):
    if request.method == 'GET':
        try:
            # Recherchez l'emploi professionnel par CIN de l'enseignant
            emploi = EmploiProf.objects.filter(CinEnseignant=cin)
        except EmploiProf.DoesNotExist:
            return Response({"message": "EmploiProf not found"}, status=status.HTTP_404_NOT_FOUND)

        # Liste des séances de l'emploi trouvé
        seances_list = []

        # Parcourir chaque emploi et chaque séance
        for emploi_item in emploi:
            for seance in emploi_item.Seances:
                seance_data = {
                    'horaire': seance.horaire,
                    'matiere': seance.matiere,
                    'sale': seance.sale,
                    'jourSemaine': seance.jourSemaine,
                    'groupe': seance.groupe,
                }
                seances_list.append(seance_data)

        return Response(seances_list, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

