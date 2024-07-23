from django.db import models
from mongoengine import Document, StringField , FileField, BooleanField

# Create your models here.


class Files(Document):
    pdf = models.FileField(upload_to='store/pdfs/')

    def __str__(self):
        return self.pdf
