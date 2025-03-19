import httplib2
import re
import base64

http = httplib2.Http()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def getData(isbn, returnImage=False):
    print(isbn)
    url = f"https://isbndb.com/book/{isbn}"
    response, content = http.request(url, 'GET',headers=headers)        
    if response['status'] == '200':
        image=""
        if returnImage:
            pattern = r'data="([^"]+)"'
            urlImage = re.findall(pattern, content.decode("utf-8"))
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
    else:
        print("Erreur : Statut de la réponse :", response['status'])
    raise "Not Found"