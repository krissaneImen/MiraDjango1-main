from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Soutenance
from .Serializers import SoutenanceSerializer

@api_view(['POST'])
def create_soutenance(request):
    soutenance_serializer = SoutenanceSerializer(data=request.data)
    if soutenance_serializer.is_valid():
        soutenance_serializer.save()
        return Response(soutenance_serializer.data, status=status.HTTP_201_CREATED)
    return Response(soutenance_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PUT'])
def update_soutenance(request, groupe_id):
    try:
        soutenance = Soutenance.objects.get(id=groupe_id)
    except Soutenance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    soutenance_data = request.data
    serializer = SoutenanceSerializer(soutenance, data=soutenance_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_soutenance_by_id(request, groupe_id):
    try:
        soutenance = Soutenance.objects.get(id=groupe_id)
    except Soutenance.DoesNotExist:
        return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = SoutenanceSerializer(soutenance)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_all_soutenances(request):
    try:
        soutenances = Soutenance.objects.all()
        serialized_groupes = [soutenance.to_dict() for soutenance in soutenances]
        return Response(serialized_groupes, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['DELETE'])
def delete_soutenance(request, groupe_id):
    try:
        soutenance = Soutenance.objects.get(id=groupe_id)
    except Soutenance.DoesNotExist:
        return Response({"message": "Soutenance  not found"}, status=status.HTTP_404_NOT_FOUND)

    soutenance.delete()
    return Response({"message": "Soutenance deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def soutenance_list(request):
    soutenances = Soutenance.objects.all()
    serialized_groupes = [soutenance.to_dict() for soutenance in soutenances]
    return Response(serialized_groupes, status=status.HTTP_200_OK)
   

@api_view(['GET'])
def get_students_by_encadrant_cin(request, cin_encadreur):
    try:
        soutenances = Soutenance.objects.filter(CinEncadreur=cin_encadreur)
        if not soutenances:
            return Response({"message": "Encadrant not found"}, status=status.HTTP_404_NOT_FOUND)

        students_list = []
        for soutenance in soutenances:
            students_list.extend([etudiant.to_dict() for etudiant in soutenance.Etudiants])
        return Response(students_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_students_by_president_jury_cin(request, cin_president_jury):
    try:
        soutenances = Soutenance.objects.filter(CinPresidentJuri=cin_president_jury)
        if not soutenances:
            return Response({"message": "President du jury not found"}, status=status.HTTP_404_NOT_FOUND)

        students_list = []
        for soutenance in soutenances:
            students_list.extend([etudiant.to_dict() for etudiant in soutenance.Etudiants])
        return Response(students_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_students_by_rapporteur_cin(request, cin_rapporteur):
    try:
        soutenances = Soutenance.objects.filter(CinRaporteur=cin_rapporteur)
        if not soutenances:
            return Response({"message": "Rapporteur not found"}, status=status.HTTP_404_NOT_FOUND)

        students_list = []
        for soutenance in soutenances:
            students_list.extend([etudiant.to_dict() for etudiant in soutenance.Etudiants])
        return Response(students_list, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


