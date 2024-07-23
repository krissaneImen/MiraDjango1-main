"""
URL configuration for miraDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,  include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('User.urls')),
    path('EmploiTemps/', include('EmploiTemps.urls')),
    path('profil/', include('Profil.urls')),
    path('nouv/', include('Nouveaute.urls')),
    path('formation/', include('Formation.urls')),
    path('manifestation/', include('Manifestation.urls')),
    path('documentation/', include('Documentation.urls')),
    path('stageEvaluation/', include('EvaluationStage.urls')),
    path('fichier/', include('File.urls')),
    path('type/', include('Type.urls')),
    path('demande/', include('Demande.urls')),
    path('groupe/', include('Groupe.urls')),
    path('emploi/', include('Emploi.urls')),
    path('enseignantEmploi/', include('EmploiEnseignant.urls')),
    path('photocopie/', include('Photocopie.urls')),
    path('attestation/', include('Attestation.urls')),
    path('calendrier/', include('Calendrier.urls')),
    path('actualite/', include('Actualite.urls')),
    path('reglement/', include('Reglement.urls')),
    path('GestionType/', include('GestionType.urls')),
    path('journale/', include('DetailJournale.urls')),
    path('tache/', include('Tache.urls')),
    path('evaluation/', include('Evaluation.urls')),
    path('stage/', include('Stage.urls')),
    path('abscence/', include('Abscence.urls')),
    path('rapport/', include('Rapport.urls')),
    path('avis/', include('Avis.urls')),
    path('emploiProf/', include('EmploiProf.urls')),
    path('soutenance/', include('Soutenance.urls')),
    path('conversation/', include('Conversation.urls')),
    path('cours/', include('Cours.urls')),
    path('client/', include('Client.urls')),
    path('', include('Fichier.urls')),
]
