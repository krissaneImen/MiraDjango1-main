### Mira Backend avec Django

#### Aperçu
Mira est un projet Django qui utilise MongoEngine pour la gestion de la base de données. Ce fichier README fournit des instructions pour configurer et exécuter la partie backend de l'application Mira.

#### Prérequis
Assurez-vous d'avoir les éléments suivants installés :
- **Python** : Version 3.8 ou supérieure
- **Django** : Version 4.x
- **MongoEngine** : Version 0.24.0 ou supérieure
- **Django REST Framework** : Version 3.14.0 ou supérieure
- **Google Generative AI** (si utilisé) : Pour les fonctionnalités spécifiques

#### Installation

**Installation des dépendances**
1. Créez un environnement virtuel et activez-le :

   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
   ```

2. Installez les dépendances requises :

   ```sh
   pip install django mongoengine djangorestframework google-generativeai
   ```

3. Assurez-vous que toutes les dépendances sont listées dans un fichier `requirements.txt` pour faciliter la gestion des packages :

   ```sh
   pip freeze > requirements.txt
   ```

#### Configuration du Projet

1. **Configuration MongoEngine**
   Assurez-vous que MongoEngine est correctement configuré dans votre fichier `settings.py` :

   ```python
   from mongoengine import connect

   connect(
       db='mira_db',
       host='localhost',
       port=27017
   )
   ```

2. **Définition des Modèles**
   Voici quelques exemples de modèles définis dans `models.py` :

   ```python
   from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField, ListField, FileField
   from django.utils import timezone

   class FichePresence(Document):
       date = DateTimeField(default=timezone.now)
       etudiant = StringField()
       presente = BooleanField()

   class Etudiant(Document):
       nom = StringField()
       email = EmailField()
   ```

3. **Définition des Sérialiseurs**
   Voici des exemples de sérialiseurs définis dans `Serializers.py` :

   ```python
   from rest_framework import serializers
   from .models import FichePresence, Etudiant

   class FichePresenceSerializer(serializers.Serializer):
       date = serializers.DateTimeField()
       etudiant = serializers.CharField()
       presente = serializers.BooleanField()

   class EtudiantSerializer(serializers.Serializer):
       nom = serializers.CharField()
       email = serializers.EmailField()
   ```

4. **Définition des Vues**
   Les vues sont définies dans `views.py` :

   ```python
   from rest_framework.decorators import api_view
   from rest_framework.response import Response
   from rest_framework import status
   from .models import FichePresence, Etudiant
   from .Serializers import FichePresenceSerializer, EtudiantSerializer

   @api_view(['GET', 'POST'])
   def fiche_presence_list(request):
       if request.method == 'GET':
           fiches = FichePresence.objects.all()
           serializer = FichePresenceSerializer(fiches, many=True)
           return Response(serializer.data)

       if request.method == 'POST':
           serializer = FichePresenceSerializer(data=request.data)
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   ```

5. **Configuration des URL**
   Ajoutez les routes dans `urls.py` :

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('fiches/', views.fiche_presence_list),
       # Ajoutez d'autres routes ici
   ]
   ```

#### Exécution du Serveur
Pour lancer le serveur de développement Django, utilisez la commande suivante :

```sh
python manage.py runserver
```

#### Développement et Tests
- **Tests** : Utilisez les commandes Django pour exécuter les tests :

  ```sh
  python manage.py test
  ```

- **Débogage** : Assurez-vous que vous utilisez un débogueur pour suivre les erreurs et les exceptions dans votre code.

#### Ressources Supplémentaires
- [Documentation Django](https://docs.djangoproject.com/)
- [Documentation MongoEngine](https://docs.mongoengine.org/)
- [Documentation Django REST Framework](https://www.django-rest-framework.org/)

#### Contribution
Pour contribuer à ce projet, veuillez forker le dépôt, apporter vos modifications, et soumettre une pull request. Assurez-vous que votre code respecte les normes de codage du projet et inclut des tests pour les nouvelles fonctionnalités.

---

Bon développement !
