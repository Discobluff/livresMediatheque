import httplib2
import json
import re
import base64

http = httplib2.Http()

# Clé API Google Books
api_key = "AIzaSyCahFEnMNv3luknZLZ6dGYLcC901zGD5QE"

# URL de l'API avec le paramètre ISBN

def getData(isbn, returnImage=False):
    # print(isbn)
    # isbn = isbn10From13(str(isbn))
    print(isbn)
    # url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}"
    # url = f"https://isbnsearch.org/isbn/{isbn}"
    # url = "https://api2.isbndb.com/book/9782258152793"
    url = f"https://isbndb.com/book/{isbn}"
    # Envoi de la requête GET
    response, content = http.request(url, 'GET')        
    if response['status'] == '200':
        image=""
        if returnImage:
            pattern = r'data="([^"]+)"'
            urlImage = re.findall(pattern, content.decode("utf-8"))
            print(urlImage)
            if len(urlImage)>0:
                urlImage = urlImage[0]
                r, c = http.request(urlImage, "GET")
                if r.status == 200:
                    encoded_string = base64.b64encode(c).decode('utf-8')
                    image = encoded_string
        content = content.split(b"<table")[1].split(b"</table>")[0]
        title = content.split(b"<td>")[1].split(b"</td>")[0].decode("utf-8")          
        author = content.split(b"<td>")[4].split(b"</td>")[0].split(b">")[1].split(b"<")[0].decode("utf-8")
        return title.replace("(French Edition)","").replace("&#039;","'"),author,image
        # print(content)
        # book_data = content.json()
        # book_data = json.loads(content) 
        # if "items" in book_data:
        #     book_info = book_data["items"][0]["volumeInfo"]
        #     titre = book_info.get("title")
        #     authors = book_info.get("authors")
        #     return titre,authors
        # else:
        #     print("Aucun livre trouvé avec cet ISBN.")
    else:
        print("Erreur : Statut de la réponse :", response['status'])
    raise "Not Found"