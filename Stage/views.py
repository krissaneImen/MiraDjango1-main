from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from Soutenance.models import Soutenance
from .models import Stage
from .Serializers import StageSerializer
from django.http import JsonResponse

@api_view(['POST'])
def create_Stage(request):
    if request.method == 'POST':
        stage_serializer = StageSerializer(data=request.data)
        if stage_serializer.is_valid():
            stage_serializer.save()
            return Response(stage_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(stage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['PUT'])
def update_Stage(request, pk):
    try:
        stage = Stage.objects.get(id=pk)
    except Stage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    groupe_data = request.data
    serializer = StageSerializer(stage, data=groupe_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_Stage_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            tache = Stage.objects.get(id=groupe_id)
        except Stage.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)
        tache_data = {
                'id': str(tache.id),  # Conversion en chaîne pour l'ID si nécessaire
                'anneeUniversitaire': tache.anneeUniversitaire,
                'Departement': tache.Departement,
                'NomEtudiant': tache.NomEtudiant,
                'NatureStage': tache.NatureStage,
                'DateJeri': tache.DateJeri,
                'RemiseRapport': tache.RemiseRapport,
                'PeriodeStage': tache.PeriodeStage,
                
            }
        serializer = StageSerializer(tache)
        return Response(tache_data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_all_Stage(request ):
    if request.method == 'GET':
        stages = Stage.objects.all()
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),  # Conversion en chaîne pour l'ID si nécessaire
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
                
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['DELETE'])
def delete_Stage(request, pk):
    try:
        stage = Stage.objects.get(pk=pk)
    except Stage.DoesNotExist:
        return JsonResponse({"error": "Tache not found"}, status=404)
    
    if request.method == 'DELETE':
        stage.delete()
        return JsonResponse({"message": "Tache deleted successfully"}, status=200)


from datetime import datetime

@api_view(['PUT'])
def Remise_Rapport(request):
    if request.method == 'PUT':
        # Récupérer les données de la requête
        stage_data = request.data
        # Vérifier si la liste des Cins est présente dans les données de la requête
        if 'cins' not in stage_data or not isinstance(stage_data['cins'], list):
            return Response({"message": "Cins must be provided as a list."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        cins = stage_data['cins']
        results = []
        
        for cin in cins:
            try:
                stage = Stage.objects.get(CinEtudiant=cin)
            except Stage.DoesNotExist:
                results.append({"cin": cin, "status": "not found"})
                continue

            # Vérifier si le champ "RemiseRapport" est présent dans les données de la requête
            if 'RemiseRapport' in stage_data:
                # Vérifier si la valeur envoyée est une date valide
                try:
                    remise_rapport_date = datetime.strptime(stage_data['RemiseRapport'], '%Y-%m-%d').date()
                except ValueError:
                    results.append({"cin": cin, "status": "invalid date format"})
                    continue
                # Mettre à jour le champ "RemiseRapport"
                stage.RemiseRapport = remise_rapport_date

            # Utiliser le sérialiseur pour valider et enregistrer les modifications
            serializer = StageSerializer(stage, data=stage_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                results.append({"cin": cin, "status": "updated"})
            else:
                results.append({"cin": cin, "status": "validation error", "errors": serializer.errors})
        
        return Response(results, status=status.HTTP_200_OK)
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_Stage_DateJeri(request):
    if request.method == 'PUT':
        # Récupérer les données de la requête
        stage_data = request.data
        # Vérifier si la liste des Cins est présente dans les données de la requête
        if 'cins' not in stage_data or not isinstance(stage_data['cins'], list):
            return Response({"message": "Cins must be provided as a list."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        cins = stage_data['cins']
        results = []
        
        for cin in cins:
            try:
                stage = Stage.objects.get(CinEtudiant=cin)
            except Stage.DoesNotExist:
                results.append({"cin": cin, "status": "not found"})
                continue

            # Vérifier si le champ "DateJeri" est présent dans les données de la requête
            if 'DateJeri' in stage_data:
                # Vérifier si la valeur envoyée est une date valide
                try:
                    date_jeri = datetime.strptime(stage_data['DateJeri'], '%Y-%m-%d').date()
                except ValueError:
                    results.append({"cin": cin, "status": "invalid date format"})
                    continue
                # Mettre à jour le champ "DateJeri"
                stage.DateJeri = date_jeri

            # Utiliser le sérialiseur pour valider et enregistrer les modifications
            serializer = StageSerializer(stage, data=stage_data, partial=True)
            if serializer.is_valid():
                serializer.save()
                results.append({"cin": cin, "status": "updated"})
            else:
                results.append({"cin": cin, "status": "validation error", "errors": serializer.errors})
        
        return Response(results, status=status.HTTP_200_OK)
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['PUT'])
def update_fields(request):
    if request.method == 'PUT':
        stage_data = request.data
        if 'cins' not in stage_data or not isinstance(stage_data['cins'], list):
            return Response({"message": "Cins must be provided as a list."},
                            status=status.HTTP_400_BAD_REQUEST)
        
        cins = stage_data['cins']
        results = []
        
        for cin in cins:
            try:
                stage = Stage.objects.get(CinEtudiant=cin)
            except Stage.DoesNotExist:
                results.append({"cin": cin, "status": "not found"})
                continue


            stage.NomRaporteur = stage_data.get('NomRaporteur', 'Non attribué')
            stage.CinRaporteur = stage_data.get('CinRaporteur', '')
            stage.NomPresidentJuri = stage_data.get('NomPresidentJuri', 'Non attribué')
            stage.CinPresidentJuri = stage_data.get('CinPresidentJuri', 'Non attribué')
            stage.NomEncadreur = stage_data.get('NomEncadreur', 'Non attribué')
            stage.CinEncadreur = stage_data.get('CinEncadreur', '')

            stage.save()

            results.append({"cin": cin, "status": "updated"})
        
        return Response(results, status=status.HTTP_200_OK)
    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_Stages_par_CinEtudiant(request, cin):
    if request.method == 'GET':
        stages = Stage.objects.filter(CinEtudiant=cin)
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_Stages_par_CinEncadreur(request, cin):
    if request.method == 'GET':
        stages = Stage.objects.filter(CinEncadreur=cin)
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

# Les fonctions pour get_Stages_par_CinRapporteur et get_Stages_par_CinPresident sont similaires à celles ci-dessus


@api_view(['GET'])
def get_Stages_par_CinRapporteur(request, cin):
    if request.method == 'GET':
        stages = Stage.objects.filter(CinRapporteur=cin)
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def mes_Stage(request, cin):
    if request.method == 'GET':
        stages = Stage.objects.filter(CinEtudiant=cin)
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
                'CinEncadreur': stage.CinEncadreur,
                'NomEncadreur': stage.NomEncadreur,
                'CinPresidentJuri': stage.CinPresidentJuri,
                'NomPresidentJuri': stage.NomPresidentJuri,
                'CinRaporteur': stage.CinRaporteur,
                'NomRaporteur': stage.NomRaporteur,
                'CinEtudiant': stage.CinEtudiant,
                'NomEtudiant': stage.NomEtudiant,
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_etudiants_avec_stage(request):
    if request.method == 'GET':
        # Filtrer les stages pour obtenir ceux qui ont des étudiants avec un CinEtudiant non nul
        stages = Stage.objects.filter(CinEtudiant__ne=None).filter(CinEtudiant__ne='')
        serialized_stages = []
        for stage in stages:
            stage_data = {
                'id': str(stage.id),
                'anneeUniversitaire': stage.anneeUniversitaire,
                'Departement': stage.Departement,
                'NomEtudiant': stage.NomEtudiant,
                'CinEtudiant': stage.CinEtudiant,
                'NatureStage': stage.NatureStage,
                'DateJeri': stage.DateJeri,
                'RemiseRapport': stage.RemiseRapport,
                'PeriodeStage': stage.PeriodeStage,
                'CinEncadreur': stage.CinEncadreur,
                'NomEncadreur': stage.NomEncadreur,
                'CinPresidentJuri': stage.CinPresidentJuri,
                'NomPresidentJuri': stage.NomPresidentJuri,
                'CinRaporteur': stage.CinRaporteur,
                'NomRaporteur': stage.NomRaporteur,
                
            }
            serialized_stages.append(stage_data)
        return Response(serialized_stages, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    



@api_view(['GET'])
def get_students_by_rapporteur_cin(request, cin_president_jury):
    try:
        # Filtrer les soutenances par le CIN du président du jury, du rapporteur ou de l'encadreur
        soutenances = Soutenance.objects.filter(
            CinRaporteur=cin_president_jury
        ) | Soutenance.objects.filter(
            CinEncadreur=cin_president_jury
        ) | Soutenance.objects.filter(
            CinPresidentJuri=cin_president_jury
        )

        # Vérifier si des soutenances ont été trouvées
        if soutenances.exists():
            # Extraire les CIN des étudiants associés à ces soutenances
            students_cins = set()
            for soutenance in soutenances:
                for etudiant in soutenance.Etudiants.all():
                    students_cins.add(etudiant.Cin)

            # Récupérer les journaux des étudiants
            journales = Stage.objects.filter(Cin__in=students_cins)
            serialized_journales = StageSerializer(journales, many=True).data

            return Response(serialized_journales, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Aucune soutenance trouvée pour ce président de jury"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mongoengine.queryset.visitor import Q
from .models import  Stage

@api_view(['GET'])
def get_students_by_president_jury_cin(request, cin_president_jury):
    try:
        # Filtrer les soutenances par le CIN du président du jury
        soutenances = Soutenance.objects.filter(
            Q(CinRaporteur=cin_president_jury) |
            Q(CinEncadreur=cin_president_jury) |
            Q(CinPresidentJuri=cin_president_jury)
        )

        # Vérifier si des soutenances ont été trouvées
        if soutenances:
            # Extraire les CIN des étudiants associés à ces soutenances
            students_cins = set()
            for soutenance in soutenances:
                for etudiant in soutenance.Etudiants:
                    students_cins.add(etudiant.Cin)

            # Récupérer les journaux des étudiants
            stages = Stage.objects.filter(CinEtudiant__in=students_cins)
            serialized_journales = []
            for stage in stages:
                journale_data = {
                    'id': str(stage.id),
                    'anneeUniversitaire': stage.anneeUniversitaire,
                    'Departement': stage.Departement,
                    'CinEncadreur': stage.CinEncadreur,
                    'NomEncadreur': stage.NomEncadreur,
                    'CinPresidentJuri': stage.CinPresidentJuri,
                    'NomPresidentJuri': stage.NomPresidentJuri,
                    'CinRaporteur': stage.CinRaporteur,
                    'NomRaporteur': stage.NomRaporteur,
                    'CinEtudiant': stage.CinEtudiant,
                    'NomEtudiant': stage.NomEtudiant,
                    'NatureStage': stage.NatureStage,
                    'DateJeri': stage.DateJeri,
                    'RemiseRapport': stage.RemiseRapport,
                    'PeriodeStage': stage.PeriodeStage,
                }
                serialized_journales.append(journale_data)

            return Response(serialized_journales, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Aucune soutenance trouvée pour ce président de jury"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

    