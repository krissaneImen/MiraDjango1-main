import requests

url = 'http://localhost:8000/cours/chat/'

# Message à envoyer au chatbot
message = "Bonjour !"

# Envoyer une requête POST avec le message
response = requests.post(url, data={'message': message})

# Afficher la réponse du chatbot
print(response.json())
