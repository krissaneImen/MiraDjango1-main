from mongoengine import Document, StringField 


class TypeReglement(Document):
    cible = StringField(max_length=200, null=False )
    name = StringField(max_length=200, null=False )
