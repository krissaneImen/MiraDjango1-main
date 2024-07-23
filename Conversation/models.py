from django.utils import timezone
from mongoengine import Document, StringField, ListField,DateField ,EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField


class Message(EmbeddedDocument):
    user = StringField(max_length=200)
    Contenu = StringField()
    date = DateField( null=True, verbose_name='Date')
    heure = StringField()
    def to_dict(self):
        return {
            'user': self.user,
            'Contenu': self.Contenu,
            'date': self.date,
            'heure': self.heure
        }
    


class Conversation(Document):
    Titre = StringField(max_length=200, verbose_name='intitule')
    CinUser = StringField(max_length=200, verbose_name='CinUser')
    dateConversation = DateField( null=True, verbose_name='Date')
    Messages = ListField(EmbeddedDocumentField(Message), verbose_name='Etudiants')

    def create_message(self, **kwargs):
        message = Message(**kwargs)
        self.Messages.append(message)
        self.save()
        return message

    
    def to_dict(self):
        return {
            'id': str(self.id),  # Retournez l'ID du groupe
            'Titre': self.Titre,
            'CinUser': self.CinUser,
            'dateConversation': self.dateConversation,
            'Messages': [message.to_dict() for message in self.Messages]
        }
