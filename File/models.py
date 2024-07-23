from mongoengine import Document, StringField,  FileField, BooleanField
from django.utils import timezone

class PDFFile(Document):
    name = StringField(max_length=200, unique=True, required=True, verbose_name='Numéro de carte d\'identité nationale')
    pdf_file = FileField(upload_to='store/pdfs/')  
    type = StringField(max_length=150, null=True)
    etudiant = BooleanField(default=False)
    enseignant = BooleanField(default=False)
    administratif = BooleanField(default=False)
    administrateur = BooleanField(default=False)


