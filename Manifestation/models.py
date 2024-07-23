from django.utils import timezone
from mongoengine import Document, StringField, BooleanField, IntField, DateField, EmailField, ImageField, BinaryField

class Manifestation(Document):
    Identifiant = StringField(max_length=230, unique=True, required=True, verbose_name='Numéro de carte d\'identité nationale')
    intitule = StringField(max_length=200, verbose_name='Intitulé')
    slogan = StringField(max_length=200, verbose_name='slogan')
    description = StringField(max_length=500, verbose_name='Description')
    dateDebut = DateField(null=True, verbose_name='Date de Formation')
    dateFin = DateField(default=timezone.now, null=True, verbose_name='Date de publication')
    lieuManifestation = StringField(max_length=100, verbose_name='Lieu de Formation')
    responsables = StringField(max_length=200, verbose_name='Responsables')
    formateurs = StringField(max_length=200, verbose_name='Formateur')
    lienInscription = StringField(max_length=100, verbose_name='Lien Inscription')
    phoneNumber = IntField(default=0, verbose_name='Numéro de Téléphone')
    poster = StringField(blank=True, default='', verbose_name='Poster')
    categorie = StringField(max_length=50, verbose_name='Catégorie')
    prix = IntField(default=0, verbose_name='Prix')
    email = EmailField( verbose_name='Email')
    lien = StringField(max_length=200, verbose_name='Lien')
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)
