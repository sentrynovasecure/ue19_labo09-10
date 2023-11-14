import requests

def get_pun():
    response = requests.get("https://api.punapi.com/pun")
    if response.status_code == 200:
        return response.json()['pun']
    else:
        return "Erreur lors de la récupération d'un jeu de mots."

if __name__ == "__main__":
    print(get_pun())
