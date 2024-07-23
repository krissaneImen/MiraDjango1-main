from django.utils import timezone
from mongoengine import Document, StringField, ListField ,EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField


# models.py

class Etudiant(EmbeddedDocument):
    NomEtudiant = StringField(max_length=200)
    Cin = StringField(max_length=20)

    def to_dict(self):
        return {
            'NomEtudiant': self.NomEtudiant,
            'Cin': self.Cin
        }



class Groupe(Document):
    nomGroupe = StringField(max_length=200, verbose_name='intitule')
    Licence = StringField(max_length=500, verbose_name='description')
    Niveau = StringField(max_length=500, verbose_name='description')
    Specialite = StringField(max_length=500, verbose_name='description')
    Anneeuniversitaire = StringField(max_length=100, verbose_name='Lieu de Formation')
    Etudiants = ListField(EmbeddedDocumentField(Etudiant), verbose_name='Etudiants')

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

    def to_dict(self):
        return {
            'id': str(self.id),  # Return the ID of the group
            'nomGroupe': self.nomGroupe,
            'Licence': self.Licence,
            'Niveau': self.Niveau,
            'Specialite': self.Specialite,
            'Anneeuniversitaire': self.Anneeuniversitaire,
            'Etudiants': [etudiant.to_dict() for etudiant in self.Etudiants]
        }
