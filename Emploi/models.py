# models.py
from mongoengine import Document, StringField, FileField ,ListField

class ClassSchedule(Document):
    anneeUniversitaire = StringField(required=True)
    semestre = StringField(required=True)
    classes = StringField(required=True)
    type = StringField(required=True)
    emploiFile = FileField(required=True)  # Use FileField instead of StringField for file uploads
