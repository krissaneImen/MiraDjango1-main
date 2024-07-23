# Django Model
from mongoengine import Document, StringField, DateTimeField, FileField

class UploadedFile(Document):
    name = StringField()
    file = FileField(upload_to='uploads/')
    uploaded_at = DateTimeField(auto_now_add=True)
