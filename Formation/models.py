from django.utils import timezone
from mongoengine import Document, StringField,  BooleanField, IntField, DateField, EmailField, ImageField, BinaryField

class Formation(Document):
    Identifiant = StringField(max_length=20, unique=True, required=True, verbose_name='Numéro de carte d\'identité nationale')
    intitule = StringField(max_length=500, verbose_name='intitule')
    description = StringField(max_length=1000, verbose_name='description')
    dateDeFormation = DateField( null=True, verbose_name='Date de Formation')
    lieuFormation = StringField(max_length=100, verbose_name='Lieu de Formation')
    datePublication = DateField( default=timezone.now, null=True, verbose_name='Date de publication')
    responsable = StringField(max_length=100, verbose_name='responsable')
    formateur = StringField(max_length=100, verbose_name='formateur')
    isPublished = BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    lienInscription = StringField(max_length=500,verbose_name='lienInscription')
    phoneNumber = IntField(default=0)
    poster = StringField(blank=True, default='') 
    codeQrInscription = StringField(blank=True, default='')
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)

