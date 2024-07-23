from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, EmailField
from django.utils import timezone

class User(Document):
    cin = StringField(max_length=128, unique=True)
    phoneNumber = IntField(default=0)
    dateDeDelivrance = DateTimeField(default=timezone.now)
    email = EmailField(unique=True)
    password = StringField(max_length=128)
    statut = StringField(max_length=150, null=True)
    lastLogin = DateTimeField(default=timezone.now)
    isSuperuser = BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    firstName = StringField(max_length=150, verbose_name='first name')
    titre = StringField(default='',max_length=150, verbose_name='Titre')
    lastName = StringField(max_length=150, verbose_name='last name')
    isActive = BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
    resetPassword = BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')
