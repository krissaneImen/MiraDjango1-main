# Mira Django Backend

## Aperçu

Le backend de Mira est construit avec Django, utilisant MongoEngine pour la gestion des modèles de données et Django REST Framework pour les API. Ce fichier README vous guidera à travers la configuration et l'exécution du backend.

## Prérequis

Assurez-vous que vous avez les éléments suivants installés sur votre machine :
- **Python** : Version 3.8 ou supérieure
- **Django** : Version 4.2 ou supérieure
- **MongoEngine** : Pour la gestion des modèles MongoDB
- **Django REST Framework** : Pour les API
- **MongoDB** : Serveur de base de données

## Installation

1. **Cloner le dépôt**

   ```sh
   git clone https://github.com/yourusername/mira-django-backend.git
   cd mira-django-backend
   ```

2. **Créer un environnement virtuel et l'activer**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances**

   ```sh
   pip install -r requirements.txt
   ```

4. **Configurer MongoDB**

   Assurez-vous que MongoDB est en cours d'exécution. La connexion à MongoDB est configurée dans `settings.py`.

## Configuration

1. **Paramétrer les variables d'environnement**

   Vous devez configurer les variables d'environnement nécessaires pour le projet. Ajoutez un fichier `.env` à la racine du projet avec les informations suivantes :

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   EMAIL_HOST='mail.coursenligne.info'
   EMAIL_PORT=465
   EMAIL_HOST_USER='adminmira@coursenligne.info'
   EMAIL_HOST_PASSWORD='1M0tdepasse---'
   ```

2. **Configurer la base de données**

   La connexion à MongoDB est définie dans `settings.py`. Assurez-vous que l'URL de connexion est correcte :

   ```python
   mongoengine.connect(
       db='dbmira', 
       host='mongodb://localhost:27017/dbmira'
   )
   ```

## Exécution

1. **Lancer le serveur Django**

   ```sh
   python manage.py runserver
   ```

2. **Accéder à l'API**

   Vous pouvez accéder à l'API via `http://localhost:8000/`. Assurez-vous que vos routes API sont correctement configurées dans les fichiers `urls.py` des applications.

## Structure du projet

```plaintext
miraDjango/
│
├── manage.py                # Script pour exécuter des commandes Django
├── miraDjango/              # Répertoire principal du projet
│   ├── __init__.py
│   ├── settings.py          # Configuration du projet Django
│   ├── urls.py              # Configuration des routes URL
│   └── wsgi.py              # Configuration WSGI pour le déploiement
├── app_name/                # Répertoire de l'application (remplacez 'app_name' par le nom réel)
│   ├── __init__.py
│   ├── models.py            # Définition des modèles de données avec MongoEngine
│   ├── views.py             # Logique des vues
│   ├── serializers.py       # Sérialiseurs pour les API
│   ├── urls.py              # Routes spécifiques à l'application
│   └── forms.py             # Formulaires Django
├── requirements.txt         # Liste des dépendances Python
└── README.md                # Documentation du projet
```

## Développement et tests

Pour exécuter les tests, utilisez :

```sh
python manage.py test
```

## Ressources supplémentaires

- [Documentation Django](https://docs.djangoproject.com/en/4.2/)
- [Documentation MongoEngine](https://docs.mongoengine.org/)
- [Documentation Django REST Framework](https://www.django-rest-framework.org/)

## Contribution

Si vous souhaitez contribuer à ce projet, veuillez forker le dépôt et soumettre une pull request. Assurez-vous que votre code respecte les normes de codage du projet et inclut des tests pour les nouvelles fonctionnalités.

---

Bon développement !
