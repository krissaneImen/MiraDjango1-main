from mongoengine import Document, StringField, DateField

class Stage(Document):
    anneeUniversitaire = StringField(required=True)
    Departement = StringField(null=True, required=True)
    NomEtudiant = StringField(null=True, required=True)
    CinEtudiant = StringField(null=True, required=True)
    NomRaporteur = StringField(null=True, required=False ,default="Non attribué" )
    CinRaporteur = StringField(null=True, required=False)
    NomPresidentJuri = StringField( required=False ,default="Non attribué")
    CinPresidentJuri = StringField(null=True, required=False,default="Non attribué")
    NomEncadreur = StringField( required=False,default="Non attribué")
    CinEncadreur = StringField(null=True, required=False)
    NatureStage = StringField(null=True, required=False)
    DateJeri = DateField( required=False)
    RemiseRapport = DateField( required=False)
    PeriodeStage = StringField(required=True)
