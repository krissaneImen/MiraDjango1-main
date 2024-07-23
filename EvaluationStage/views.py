from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import EvaluationStage
from .Serializers import EvaluationStageSerializer
from django.http import JsonResponse

@api_view(['POST'])
def create_Evaluation(request):
    if request.method == 'POST':
        evaluation_serializer = EvaluationStageSerializer(data=request.data)
        if evaluation_serializer.is_valid():
            evaluation_serializer.save()
            return Response(evaluation_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(evaluation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def update_Evaluation(request, groupe_id):
    try:
        evaluation = EvaluationStage.objects.get(id=groupe_id)
    except EvaluationStage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    groupe_data = request.data
    serializer = EvaluationStageSerializer(evaluation, data=groupe_data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_Evaluation_by_id(request, groupe_id):
    if request.method == 'GET':
        try:
            evaluation = EvaluationStage.objects.get(id=groupe_id)
        except EvaluationStage.DoesNotExist:
            return Response({"message": "Groupe not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EvaluationStageSerializer(evaluation)
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_all_Evaluations(request):
    if request.method == 'GET':
        evaluations = EvaluationStage.objects.all()
        serialized_Evaluations = []
        for evaluation in evaluations:
            journale_data = {
                'id': str(evaluation.id),  # Conversion en chaîne pour l'ID si nécessaire
                'idStage': evaluation.idJournale,
                'DateEvaluation': evaluation.Cin,
                'CinEtudiant': evaluation.NomRapporteur,
                'NomEtudiant': evaluation.FormeExpression,
                'Groupe': evaluation.FormePesentation,
                'SocieteAccueil': evaluation.PresentationEntreprise,
                'CinPresident': evaluation.ValeurScien,
                'President': evaluation.EffortPersonnel,
                'Rapporteur': evaluation.Rapporteur,
                'CinRapporteur': evaluation.CinRapporteur,
                'Rapport': evaluation.Rapport,
                'FondRapport': evaluation.FondRapport,
                'formeRapport': evaluation.formeRapport,
                'JournaleStage': evaluation.JournaleStage,
                'QualiteJournale': evaluation.QualiteJournale,
                'RemarqueEncadrantPro': evaluation.RemarqueEncadrantPro,
                'QualitePresentation': evaluation.QualitePresentation,
                'QualiteSpeech': evaluation.QualiteSpeech,
                'ReactionQuestion': evaluation.ReactionQuestion,
                'clarteExpression': evaluation.clarteExpression,
                'CapaciteConvaincre': evaluation.CapaciteConvaincre,
                'ValiditeStage': evaluation.ValiditeStage,
                'NoteFinale': evaluation.NoteFinale,
                'Observation': evaluation.Observation,
                
            }
            serialized_Evaluations.append(journale_data)
        return Response(serialized_Evaluations, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def get_Evaluation(request , id):
    if request.method == 'GET':
        evaluations = EvaluationStage.objects.filter(  idJournale=id)
        for evaluation in evaluations:
            evaluation_data = {
                'id': str(evaluation.id),  # Conversion en chaîne pour l'ID si nécessaire
                'idStage': evaluation.idStage,
                'DateEvaluation': evaluation.DateEvaluation,
                'CinEtudiant': evaluation.CinEtudiant,
                'NomEtudiant': evaluation.NomEtudiant,
                'Groupe': evaluation.Groupe,
                'SocieteAccueil': evaluation.SocieteAccueil,
                'CinPresident': evaluation.CinPresident,
                'President': evaluation.President,
                'Rapporteur': evaluation.Rapporteur,
                'CinRapporteur': evaluation.CinRapporteur,
                'FondRapport': evaluation.FondRapport,
                'formeRapport': evaluation.formeRapport,
                'JournaleStage': evaluation.JournaleStage,
                'QualiteJournale': evaluation.QualiteJournale,
                'RemarqueEncadrantPro': evaluation.RemarqueEncadrantPro,
                'Presentation': evaluation.Presentation,
                'QualitePresentation': evaluation.QualitePresentation,
                'QualiteSpeech': evaluation.QualiteSpeech,
                'ReactionQuestion': evaluation.ReactionQuestion,
                'clarteExpression': evaluation.clarteExpression,
                'CapaciteConvaincre': evaluation.CapaciteConvaincre,
                'ValiditeStage': evaluation.ValiditeStage,
                'NoteFinale': evaluation.NoteFinale,
                'Observation': evaluation.Observation,
                
            }
            
        return Response(evaluation_data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_Evaluation(request, pk):
    try:
        evaluation = EvaluationStage.objects.get(pk=pk)
    except EvaluationStage.DoesNotExist:
        return JsonResponse({"error": "journale not found"}, status=404)
    
    if request.method == 'DELETE':
        evaluation.delete()
        return JsonResponse({"message": "journale deleted successfully"}, status=200)


@api_view(['GET'])
def mes_Evaluation(request, cin):
    if request.method == 'GET':
        evaluations = EvaluationStage.objects.filter(Cin=cin)
        serialized_evaluations = []
        for evaluation in evaluations:
            journale_data = {
                'id': str(evaluation.id),  # Conversion en chaîne pour l'ID si nécessaire
                'idStage': evaluation.idStage,
                'DateEvaluation': evaluation.DateEvaluation,
                'CinEtudiant': evaluation.CinEtudiant,
                'NomEtudiant': evaluation.NomEtudiant,
                'Groupe': evaluation.Groupe,
                'SocieteAccueil': evaluation.SocieteAccueil,
                'CinPresident': evaluation.CinPresident,
                'President': evaluation.President,
                'Rapporteur': evaluation.Rapporteur,
                'CinRapporteur': evaluation.CinRapporteur,
                'FondRapport': evaluation.FondRapport,
                'formeRapport': evaluation.formeRapport,
                'JournaleStage': evaluation.JournaleStage,
                'QualiteJournale': evaluation.QualiteJournale,
                'RemarqueEncadrantPro': evaluation.RemarqueEncadrantPro,
                'Presentation': evaluation.Presentation,
                'QualitePresentation': evaluation.QualitePresentation,
                'QualiteSpeech': evaluation.QualiteSpeech,
                'ReactionQuestion': evaluation.ReactionQuestion,
                'clarteExpression': evaluation.clarteExpression,
                'CapaciteConvaincre': evaluation.CapaciteConvaincre,
                'ValiditeStage': evaluation.ValiditeStage,
                'NoteFinale': evaluation.NoteFinale,
                'Observation': evaluation.Observation,
                
            }
            serialized_evaluations.append(journale_data)
            
        return Response(serialized_evaluations, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

