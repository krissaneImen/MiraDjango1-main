from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Groupe
from .Serializers import GroupeSerializer

@api_view(['POST'])
def create_groupe(request):
    if request.method == 'POST':
        groupe_serializer = GroupeSerializer(data=request.data)
        if groupe_serializer.is_valid():
            groupe_serializer.save()
            return Response(groupe_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(groupe_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_groupe(request, groupe_id):
    try:
        groupe = Groupe.objects.get(id=groupe_id)
    except Groupe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    groupe_data = request.data
    serializer = GroupeSerializer(groupe, data=groupe_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_groupe_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            groupe = Groupe.objects.get(id=groupe_id)
        except Groupe.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = GroupeSerializer(groupe)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def get_all_groupes(request):
    try:
        groupes = Groupe.objects.all()
        serialized_groupes = []
        for groupe in groupes:
            groupe_data = groupe.to_dict()
            groupe_data['Etudiants'] = [etudiant.to_dict() for etudiant in groupe.Etudiants]
            serialized_groupes.append(groupe_data)
        return Response(serialized_groupes, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Groupe

@api_view(['GET'])
def get_classe_by_cin(request, cin):
    if request.method == 'GET':
        try:
            # Recherchez parmi tous les groupes pour trouver l'étudiant
            groupes = Groupe.objects.filter(Etudiants__Cin=cin)
            if groupes:
                # Supposons que l'étudiant est unique dans les groupes
                groupe = groupes[0]
                # Supposons que la classe est déduite à partir du niveau et de la spécialité
                classe = f"{groupe.Niveau} {groupe.Specialite}"
                return Response({"classe": classe}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)
        except Groupe.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_students_by_group(request, groupe_id):
    if request.method == 'GET':
        try:
            # Récupérer le groupe spécifié par l'identifiant
            groupe = Groupe.objects.get(nomGroupe=groupe_id)
        except Groupe.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        # Liste des étudiants du groupe
        students_list = []

        # Parcourir chaque étudiant dans le groupe
        for etudiant in groupe.Etudiants:
            student_data = {
                'NomEtudiant': etudiant.NomEtudiant,
                'Cin': etudiant.Cin,
                # Ajoutez d'autres champs d'étudiant que vous voulez inclure
            }
            students_list.append(student_data)

        return Response(students_list, status=status.HTTP_200_OK)

    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['DELETE'])
def delete_groupe(request, groupe_id):
    try:
        # Recherchez le groupe par son identifiant
        groupe = Groupe.objects.get(id=groupe_id)
    except Groupe.DoesNotExist:
        return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

    # Suppression du groupe
    groupe.delete()
    return Response({"message": "Groupe deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def Groupe_list(request):
    """
    Récupère la liste des enseignants avec leur nom, prénom et CIN.

    Retour :
    - Response : réponse HTTP avec la liste des enseignants et leurs détails.
    """
    if request.method == 'GET':
        groupes = Groupe.objects.all()
        data = [{'nomGroupe': groupe.nomGroupe ,'id' : str(groupe.id)} for groupe in groupes]
        return Response(data, status=status.HTTP_200_OK)
 