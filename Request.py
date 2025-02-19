import re
import requests;

# Definite endPoint base from scryfall
endPointBase = "https://api.scryfall.com/cards"

def getId(url:str)->str:
    # Use a regular expression to find the UUID code at the end of the URL
    match = re.search(r'/([a-f0-9\-]+)\.jpg', url)
    if match:
        return match.group(1) #If the search is successful, match.group(1) returns the first captured group in the regular expression. In this case, it is the 
                                    #segment of the URL that is between the slashes / and the .jpg extension.
    return None

def getCard(id: str, lang: str) -> str:
    # We make a query to the api with the id of the card
    result = requests.get(f"{endPointBase}/{getId(id)}") # We use the getId method to obtain the id of our card
    
    # We will obtain the necessary information from the query previously made, this will be the set and the collection number
    set = result.json().get('set')
    setId = result.json().get('collector_number')

    # Get new image from api
    return getImgeLarge(set, setId, lang)

def getImgeLarge(set: str, id: str, lang: str) -> str:
    result = requests.get(f"{endPointBase}/{set}/{id}/{lang}").json().get('image_uris', {}).get('large', '') #We make a query to the API with the language information and what we have obtained before
    return result