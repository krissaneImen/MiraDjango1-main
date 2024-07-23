from django.utils import timezone
from mongoengine import Document, StringField, ListField ,EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField


class Seance(EmbeddedDocument):
    
    horaire = StringField(max_length=200)
    matiere = StringField(max_length=200)
    sale = StringField(max_length=200)
    jourSemaine = StringField(max_length=200)
    groupe = StringField(max_length=200)

    def to_dict(self):
        return {
            'horaire': self.horaire,
            'sale': self.sale,
            'matiere': self.matiere,
            'groupe': self.groupe,
            'jourSemaine': self.jourSemaine
        }
    


class EmploiProf(Document):
    anneeUniversitaire = StringField(max_length=200, verbose_name='anneeUniversitaire')
    semestre = StringField(max_length=500, verbose_name='semestre')
    NomEnseignant = StringField(max_length=500, verbose_name='NomEnseignant')
    CinEnseignant = StringField(max_length=500, verbose_name='CinEnseignant')
    type = StringField(max_length=100, verbose_name='type')
    Seances = ListField(EmbeddedDocumentField(Seance), verbose_name='Seances')

    def create_seance(self, **kwargs):
        seance = Seance(**kwargs)
        self.Seances.append(seance)
        self.save()
        return seance

    def get_Seance(self, horaire , jourSemaine):
        for Seance in self.Seances:
            if Seance.horaire == horaire and Seance.jourSemaine == jourSemaine:
                return Seance
        return None


    def to_dict(self):
        return {
            'id': str(self.id),  # Retournez l'ID du groupe
            'anneeUniversitaire': self.anneeUniversitaire,
            'semestre': self.semestre,
            'NomEnseignant': self.NomEnseignant,
            'CinEnseignant': self.CinEnseignant,
            'type': self.type,
            'Seances': [Seance.to_dict() for Seance in self.Seances]
        }
