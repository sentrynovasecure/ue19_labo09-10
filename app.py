import requests


def get_random_pun():
    response = requests.get('https://punapi.rest/api/pun')
    if response.status_code == 200:
        return response.json().get('pun', 'Aucun jeu de mots trouvé.')
    return "Erreur lors de la récupération d'un jeu de mots."


if __name__ == "__main__":
    print("Jeu de mots aléatoire: ", get_random_pun())
