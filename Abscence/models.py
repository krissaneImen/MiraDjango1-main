from mongoengine import Document, StringField, EmbeddedDocument, ListField,DateField
from mongoengine.fields import EmbeddedDocumentField
from django.utils import timezone


class Etudiant(EmbeddedDocument):
    NomEtudiant = StringField(max_length=200)
    Cin = StringField(max_length=20)
    etatAbscence = StringField(max_length=20)
    etatElimination = StringField(max_length=20)

class FichePresnce(Document):
    nomGroupe = StringField(max_length=200, verbose_name='intitule')
    Seance = StringField(max_length=500, verbose_name='Seance')
    DateSeance = DateField( default=timezone.now, null=True, verbose_name='Date de Seance')
    enseignant = StringField(max_length=500, verbose_name='enseignant')
    Sale = StringField(max_length=500, verbose_name='Sale')
    Matiere = StringField(max_length=500, verbose_name='Matiere')
    cinEnseignant = StringField(max_length=500, verbose_name='cinEnseignant')
    Anneeuniversitaire = StringField(max_length=100, verbose_name='Anneeuniversitaire')
    Etudiants = ListField(EmbeddedDocumentField(Etudiant), verbose_name='Membres')

    def create_etudiant(self, **kwargs):
        etudiant = Etudiant(**kwargs)
        self.Etudiants.append(etudiant)
        self.save()
        return etudiant

    def get_etudiant_by_Cin(self, cin):
        for etudiant in self.Etudiants:
            if etudiant.Cin == cin:
                return etudiant
        return None
