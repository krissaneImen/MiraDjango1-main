from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from .models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.models import Session
from django.http import JsonResponse


@api_view(['POST'])
def send_test_code(request):
    email = request.data.get('email')
    if email:
        # Générer le code de vérification
        
        # Mettre à jour le code de réinitialisation dans le modèle User
        try:
            
            # Envoyer l'e-mail
            send_mail(
                'Code de vérification',
                'Votre code de vérification est :ese',
                'adminmira@coursenligne.info',
                [email],
                fail_silently=False,
            )
            
            # Retourner le code de vérification dans la réponse JSON
            return JsonResponse({"code": "vbn,"}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)
    else:
        return JsonResponse({"message": "Email not provided in request"}, status=400)
   
@api_view(['POST'])
def send_verification_code(request):
    email = request.data.get('email')
    if email:
        # Générer le code de vérification
        verification_code = get_random_string(length=6, allowed_chars='0123456789')
        
        # Mettre à jour le code de réinitialisation dans le modèle User
        try:
            user = User.objects.get(email=email)
            user.reset_code = verification_code
            user.save()

            # Envoyer l'e-mail
            send_mail(
                'Code de vérification',
                f'Votre code de vérification est : {verification_code}',
                'adminmira@coursenligne.info',
                [email],
                fail_silently=False,
            )

            # Retourner le code de vérification dans la réponse JSON
            return JsonResponse({"code": verification_code}, status=200)
        except User.DoesNotExist:
            return JsonResponse({"message": "User not found"}, status=404)
    else:
        return JsonResponse({"message": "Email not provided in request"}, status=400)
   


@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)
       

        if user_serializer.is_valid() :
            # Save user
            user_serializer.save()

            # Save profile
            
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            errors = {}
            
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def user_login(request):
    """
    Authentifie un utilisateur existant.

    Paramètres:
    - request : HttpRequest - la requête HTTP contenant les informations d'identification de l'utilisateur (cin et mot de passe).

    Retour:
    - HttpResponse : réponse HTTP avec le statut approprié et un message indiquant si l'authentification a réussi ou non.
    """
    if request.method == 'POST':
        cin = request.data.get('cin')
        password = request.data.get('password')

        try:
            user = User.objects.get(cin=cin)
        except User.DoesNotExist:
            user = None

        if user is not None:
            if user.isActive:
                if check_password(password, user.password):
                    userCin=user.cin
                    
                    if user.isSuperuser:
                        user_type = "administrateur"
                    else:
                        user_type = user.statut  # Assurez-vous que statut est un champ valide dans votre modèle User

                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user_type': user_type,
                        'userCin': userCin,
                        'firstName': user.firstName,
                        'lastName':user.lastName,
                        'statut':user.statut ,
                        'cin':user.cin,
                        'userCin':user.cin,
                        'email':user.email,
                        'dateDeDelivrance':user.dateDeDelivrance,
                        'phoneNumber':user.phoneNumber,
                        
                    })
                else:
                    return Response({'message': 'Mot de passe incorrect'}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'message': 'Ce compte n\'est pas activé'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'message': 'CIN incorrect'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def validate_user_account(request, cin):
    """
    Valide le compte utilisateur en mettant à jour le champ "is_active" de False à True.

    Paramètres :
    - request : HttpRequest - la requête HTTP contenant les données de mise à jour.
    - cin : int - le numéro de CIN de l'utilisateur dont le compte doit être validé.

    Retour :
    - Response : réponse HTTP avec le statut approprié et un message indiquant si la mise à jour a réussi ou non.
    """
    try:
        user = User.objects.get(cin=cin)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user.isActive = True
        user.save()

        subject = 'Validation de compte'
        message = 'Votre compte a été validé avec succès.'
        from_email = 'adminmira@coursenligne.info'  # Remplacez par votre adresse e-mail
        to_email = [user.email]

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
        )
        return Response({"message": "Compte utilisateur validé avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT'])
def distribuer_titre(request, cin , titre):
    """
    Valide le compte utilisateur en mettant à jour le champ "is_active" de False à True.

    Paramètres :
    - request : HttpRequest - la requête HTTP contenant les données de mise à jour.
    - cin : int - le numéro de CIN de l'utilisateur dont le compte doit être validé.

    Retour :
    - Response : réponse HTTP avec le statut approprié et un message indiquant si la mise à jour a réussi ou non.
    """
    try:
        user = User.objects.get(cin=cin)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user.titre = titre
        user.save()

        return Response({"message": "Compte utilisateur validé avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def deactive_user_account(request, cin):
    """
    Valide le compte utilisateur en mettant à jour le champ "is_active" de False à True.

    Paramètres :
    - request : HttpRequest - la requête HTTP contenant les données de mise à jour.
    - user_id : int - l'identifiant de l'utilisateur dont le compte doit être validé.

    Retour :
    - HttpResponse : réponse HTTP avec le statut approprié et un message indiquant si la mise à jour a réussi ou non.
    """
    try:
        user = User.objects.get(cin=cin)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user.isActive = False
        user.save()
        subject = 'désactivation de compte'
        message = 'Votre compte a été désactivé par l\'administrateur. Veuillez contacter l\'administration pour voir le problème'
        from_email = 'adminmira@coursenligne.info'  # Remplacez par votre adresse e-mail
        to_email = [user.email]

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
        )
        return Response({"message": "Compte utilisateur desactive "}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)




@api_view(['POST'])
def send_Email(request):
    """
    Envoie un e-mail de récupération de mot de passe à l'utilisateur avec un lien sécurisé.

    Paramètres :
    - request : HttpRequest - la requête HTTP contenant l'adresse e-mail de l'utilisateur.

    Retour :
    - JsonResponse : réponse JSON avec le statut approprié et un message indiquant si l'e-mail a été envoyé avec succès.
    """
    if request.method == 'POST':
        email = request.data.get('email')

        user = get_object_or_404(User, email=email)

        # Générer un code de récupération aléatoire
        recovery_code = get_random_string(length=6, allowed_chars='0123456789')

        # Mettre à jour le code de récupération de l'utilisateur dans la base de données
        user.recovery_code = recovery_code
        user.save()

        # Envoyer l'e-mail de récupération de mot de passe
        subject = 'Réinitialisation de mot de passe'
        message = f'Utilisez le code suivant pour réinitialiser votre mot de passe : {recovery_code}'
        from_email = 'adminmira@coursenligne.info'  # Remplacez par votre adresse e-mail
        to_email = [user.email]

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
        )

        return JsonResponse({"message": "Un e-mail de récupération de mot de passe a été envoyé à votre adresse e-mail"}, status=status.HTTP_200_OK)

    return JsonResponse({"message": "Méthode non autorisée"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def get_email_by_cin(request, cin):
    """
    Récupère l'email d'un utilisateur en fonction de son numéro de CIN.

    Paramètres :
    - request : HttpRequest - la requête HTTP.
    - cin : str - le numéro de CIN de l'utilisateur.

    Retour :
    - Response : réponse HTTP avec l'email de l'utilisateur ou un message indiquant que l'utilisateur n'a pas été trouvé.
    """
    try:
        user = User.objects.get(cin=cin)
        return Response({"email": user.email}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def inactive_users(request):
    """
    Récupère tous les utilisateurs ayant la valeur False dans le champ is_active.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des utilisateurs inactifs et leur détails.
    """
    if request.method == 'GET':
        all_users = User.objects.all()
        inactive_users = [user for user in all_users if not user.isActive]
        serializer = UserSerializer(inactive_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET'])
def active_users(request):
    """
    Récupère tous les utilisateurs ayant la valeur False dans le champ is_active.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des utilisateurs inactifs et leur détails.
    """
    if request.method == 'GET':
        all_users = User.objects.all()
        inactive_users = [user for user in all_users if  user.isActive]
        serializer = UserSerializer(inactive_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    




@api_view(['POST'])
def check_cin(request):
    if request.method == 'POST':
        cin = request.data.get('cin')
        if cin is None:
            return Response({"error": "No cin provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        users_with_cin = User.objects.filter(cin=cin)
        if not users_with_cin:  # If the queryset is empty
            return Response({"exists": False, "message": "No user found with the provided cin"}, status=status.HTTP_200_OK)
        
        return Response({"exists": True}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def check_email(request):
    if request.method == 'POST':
        email = request.data.get('email')
        if email is None:
            return Response({"error": "No email provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        users_with_email = User.objects.filter(email=email)
        if not users_with_email:
            return Response({"exists": False, "message": "No user found with the provided email"}, status=status.HTTP_200_OK)
        
        return Response({"exists": True}, status=status.HTTP_200_OK)




# Méthode pour vérifier l'existence d'un identifiant (cin)
@api_view(['GET'])
def check_identifient(request, cin):
    if request.method == 'GET':
        try:
           user = User.objects.get(cin=cin)
        except User.DoesNotExist:
            return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)


# Méthode pour démarrer une session pour un utilisateur
@api_view(['POST'])
def start_session(request):
    """
    Démarre une session pour l'utilisateur actuel.
    """
    if request.method == 'POST':
        # Start a session
        request.session['is_authenticated'] = True
        return JsonResponse({'message': 'Session started successfully'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)



# Méthode pour vérifier si l'utilisateur a une session active
@api_view(['GET'])
def check_session(request):
    """
    Vérifie si l'utilisateur a une session active.
    """
    if request.method == 'GET':
        is_authenticated = request.session.get('is_authenticated', False)
        return JsonResponse({'is_authenticated': is_authenticated}, status=200)

# Méthode pour terminer la session de l'utilisateur
@api_view(['POST'])
def end_session(request):
    """
    Termine la session de l'utilisateur.
    """
    if request.method == 'POST':
        # End the session
        request.session.flush()
        return JsonResponse({'message': 'Session ended successfully'}, status=200)
    return JsonResponse({'error': 'Method not allowed'}, status=405)


 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views
 # Password Reset Views


@api_view(['GET'])
def reset_password_users(request):
    """
    Récupère tous les utilisateurs ayant la valeur False dans le champ is_active.

    Retour :
    - HttpResponse : réponse HTTP avec la liste des utilisateurs inactifs et leur détails.
    """
    if request.method == 'GET':
        all_users = User.objects.all()
        reset_password_user = [user for user in all_users if  user.reset_password]
        serializer = UserSerializer(reset_password_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def demande_reset_password(request, cin):
    """
    Valide le compte utilisateur en mettant à jour le champ "is_active" de False à True.

    Paramètres :
    - request : HttpRequest - la requête HTTP contenant les données de mise à jour.
    - user_id : int - l'identifiant de l'utilisateur dont le compte doit être validé.

    Retour :
    - HttpResponse : réponse HTTP avec le statut approprié et un message indiquant si la mise à jour a réussi ou non.
    """
    try:
        user = User.objects.get(cin=cin)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        user.reset_password = True
        user.save()
        return Response({"message": "Demande envoye  avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['PUT'])
def reset_password(request):
    email = request.data.get('email')
    new_password = request.data.get('new_password')

    if not email or not new_password:
        return Response({"message": "Veuillez fournir le cin et le nouveau mot de passe"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        # Mise à jour du mot de passe dans la base de données
        user.password = make_password(new_password)
        user.reset_password = False
        user.save()
        
        return Response({"message": "Mot de passe réinitialisé avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['GET'])
def user_detail(request, cin):
    """
    Retrieve user details by CIN.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - cin: str - the CIN of the user to retrieve.

    Returns:
    - Response: JSON response with the user details or a message indicating the user was not found.
    """
    try:
        user = User.objects.get(cin=cin)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def fetch_user_type(request, cin):

    """
    Fetches the userType for a given user.

    Parameters:
    - request: HttpRequest - the HTTP request.
    - cin: str - the CIN of the user.

    Returns:
    - Response: JSON response with the userType or a message indicating the user was not found.
    """
    try:
        user = User.objects.get(cin=cin)
        if user.isSuperuser:
            user_type = "Administrateur"
        else:
            user_type = user.statut  # Make sure statut is a valid field in your User model
        return Response({"userType": user_type}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)



@api_view(['DELETE'])
def delete_user(request, cin):
    """
    Supprime un utilisateur.

    Paramètres :
    - request : HttpRequest - la requête HTTP.
    - cin : str - le CIN de l'utilisateur à supprimer.

    Retour :
    - Response : réponse HTTP avec le statut approprié et un message indiquant si la suppression a réussi ou non.
    """
    try:
        user = User.objects.get(cin=cin)
    except User.DoesNotExist:
        return Response({"message": "Utilisateur non trouvé"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user.delete()
        subject = ' Compte supprimé '
        message = 'Votre compte a été résilié . Veuillez contacter l\'administration pour voir le problème'
        from_email = 'adminmira@coursenligne.info'  # Remplacez par votre adresse e-mail
        to_email = [user.email]

        send_mail(
            subject,
            message,
            from_email,
            to_email,
            fail_silently=False,
        )
        return Response({"message": "Utilisateur supprimé avec succès"}, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def enseignants_list(request):
    """
    Récupère la liste des enseignants avec leur nom, prénom et CIN.

    Retour :
    - Response : réponse HTTP avec la liste des enseignants et leurs détails.
    """
    if request.method == 'GET':
        enseignants = User.objects.filter(statut='enseignant')
        data = [{'nom': enseignant.firstName +" "+ enseignant.lastName , 'prenom': enseignant.firstName, 'cin': enseignant.cin} for enseignant in enseignants]
        return Response(data, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def etudiant_list(request):
    """
    Récupère la liste des enseignants avec leur nom, prénom et CIN.

    Retour :
    - Response : réponse HTTP avec la liste des enseignants et leurs détails.
    """
    if request.method == 'GET':
        etudiants = User.objects.filter(statut='etudiant')
        data = [{'nom': etudiant.firstName +" "+ etudiant.lastName , 'prenom': etudiant.firstName, 'cin': etudiant.cin} for etudiant in etudiants]
        return Response(data, status=status.HTTP_200_OK)