import requests as req

def geocode(location):
    base_url = f"https://geocoding-api.open-meteo.com/v1/search/?name={location}"
    try:
        responce = req.get(base_url)
    except:
        return None
    
    if responce.status_code != 200:
        return None
    
    data = responce.json()
    try:
        results_list = data["results"]
    except:
        return None
    if len(results_list) == 0:
        return None
    else:
        return results_list[0]

def forecast(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&am"
    results = req.get(base_url)
    if results.status_code != 200:


print("welcome to the geocode finder!")

location = "hello world"

while location != "quit":
    location = input("enter location name (or 'quit')")
    if location == "quit":
        print("Goodbye")
    else:
        results = geocode(location)
        if results == None:
            print("request failed")
        else:
            latitude = results["latitude"]
            longitude = results["longitude"]
            print(f"name: {results["name"]}, country: {results["country"]}, latitute: {latitude}, longitude: {longitude}")
            forecast(latitude, longitude)