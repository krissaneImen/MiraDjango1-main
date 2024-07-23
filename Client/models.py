from django.utils import timezone
from mongoengine import Document, StringField, ListField ,EmbeddedDocument
from mongoengine.fields import EmbeddedDocumentField


# models.py

class Contact(EmbeddedDocument):
    nom = StringField()
    valeur = StringField()

    def to_dict(self):
        return {
            'nom': self.nom,
            'valeur': self.valeur
        }
    
class Social(EmbeddedDocument):
    
    url = StringField()
    icon = StringField()
    
    def to_dict(self):
        return {
            
            'url': self.url,
            'icon': self.icon
        }


class Institut(Document):
    nomInstitut = StringField( verbose_name='nomInstitut')
    acronyme = StringField( verbose_name='acronyme')
    Directeur = StringField( verbose_name='Directeur')
    logo = StringField(blank=True, default='')
    Contacts = ListField(EmbeddedDocumentField(Contact), verbose_name='Contacts')
    Socials = ListField(EmbeddedDocumentField(Social), verbose_name='Socials')

    def create_contact(self, **kwargs):
        contact = Contact(**kwargs)
        self.Contacts.append(contact)
        self.save()
        return contact
    
    def create_social(self, **kwargs):
        social = Social(**kwargs)
        self.Socials.append(social)
        self.save()
        return social

    

    def to_dict(self):
        return {
            'id': str(self.id),  # Return the ID of the group
            'nomInstitut': self.nomInstitut,
            'acronyme': self.acronyme,
            'Directeur': self.Directeur,
            'Specialite': self.Specialite,
            'Contacts': [contact.to_dict() for contact in self.Contacts],
            'Socials': [social.to_dict() for social in self.Socials]
        }
