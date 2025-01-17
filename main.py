import requests

# ISBN du livre que vous cherchez
isbn = "9782266329439"

# Clé API Google Books
api_key = "AIzaSyCahFEnMNv3luknZLZ6dGYLcC901zGD5QE"

# URL de l'API avec le paramètre ISBN
url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}"

try:
    # Envoi de la requête GET
    response = requests.get(url)
    
    # Vérification du statut de la réponse
    if response.status_code == 200:
        # Conversion de la réponse en JSON
        book_data = response.json()
        
        # Vérification si des résultats ont été trouvés
        if "items" in book_data:
            book_info = book_data["items"][0]["volumeInfo"]
            print("Titre:", book_info.get("title"))
            print("Auteurs:", book_info.get("authors"))
        else:
            print("Aucun livre trouvé avec cet ISBN.")
    else:
        print("Erreur : Statut de la réponse :", response.status_code)

except requests.exceptions.RequestException as e:
    print("Une erreur s'est produite :", e)
