import requests
import json
import Request

# Function whit read json
def read(data: str):
    with open(data, 'r') as archivo: #Open data an load the content
        return json.load(archivo)

def write(data: str, newData: dict):
    with open(data, 'w') as archivo:
        json.dump(newData, archivo, indent=4)  # Indent for 4 spaces
    return "File is modification for successfully."

# Function modificate language of deck
def modData(data: dict, lenguage: str):
    lengs = ["en", "es", "fr", "de", "it", "pt", "ja", "ko", "ru", "zhs", "zht", "he", "la", "grc", "ar", "sa", "ph"]

    # Validate if lenguage exist
    if lenguage not in lengs:
        print(f"Not exist the language presented... Available languages : {lengs}.")
    else:
        for obj in data.get("ObjectStates", []):
            if "ContainedObjects" in obj:  # Checks if contains the object indicated
                for contained_obj in obj["ContainedObjects"]:
                    if "CustomDeck" in contained_obj:  # Checks CustomDeck is contains in the object
                        for deck_id, deck_data in contained_obj["CustomDeck"].items():
                            if "FaceURL" in deck_data:
                                print(f"Original FaceURL: {deck_data['FaceURL']}")  # Show original url
                                new_face_url = Request.getCard(deck_data["FaceURL"], lenguage)
                                if(new_face_url!=""):
                                    deck_data["FaceURL"] = new_face_url
                                print(f"Updated FaceURL: {deck_data['FaceURL']}")  #  Show modified url
                    
                    if "ContainedObjects" in contained_obj:
                        for deck_id, deck_data in contained_obj["CustomDeck"].items():
                            if "FaceURL" in deck_data:
                                print(f"Original FaceURL: {deck_data['FaceURL']}")  
                                new_face_url = Request.getCard(deck_data["FaceURL"], lenguage)
                                if(new_face_url!=""):
                                    deck_data["FaceURL"] = new_face_url
                                print(f"Updated FaceURL: {deck_data['FaceURL']}")
    return data

def main():
    data = input("Insert the json file that contains your deck:") + ".json"
    lenguage = input("Insert the language you want to assign:")
    jsonData = modData(read(data), lenguage)

    print(write(data, jsonData))

if __name__ == "__main__":
    main()
