from django.utils import timezone
from mongoengine import Document, StringField, ListField ,EmbeddedDocument ,DateField
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



class Soutenance(Document):
    NomRaporteur = StringField(null=True, required=False ,default="Non attribué" )
    CinRaporteur = StringField(null=True, required=False)
    NomPresidentJuri = StringField( required=False ,default="Non attribué")
    CinPresidentJuri = StringField(null=True, required=False,default="Non attribué")
    NomEncadreur = StringField( required=False,default="Non attribué")
    CinEncadreur = StringField(null=True, required=False)
    dateJury = DateField( null=True, verbose_name='Date')
    NatureStage = StringField(null=True, required=False)
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
            'NomRaporteur': self.NomRaporteur,
            'CinRaporteur': self.CinRaporteur,
            'NomPresidentJuri': self.NomPresidentJuri,
            'CinPresidentJuri': self.CinPresidentJuri,
            'Anneeuniversitaire': self.Anneeuniversitaire,
            'NomEncadreur': self.NomEncadreur,
            'CinEncadreur': self.CinEncadreur,
            'dateJury': self.dateJury,
            'NatureStage': self.NatureStage,
            'Etudiants': [etudiant.to_dict() for etudiant in self.Etudiants]
        }

