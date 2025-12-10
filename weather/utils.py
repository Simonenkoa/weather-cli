import requests 
 
def city_to_coords(city: str): 
    url = "https://nominatim.openstreetmap.org/search" 
    params = {"q": city, "format": "json", "limit": 1} 
    headers = {"User-Agent": "weather-cli-student/1.0"} 
    try: 
        r = requests.get(url, params=params, headers=headers, timeout=10) 
        r.raise_for_status() 
        data = r.json() 
        if not data: raise ValueError 
        return float(data[0]["lat"]), float(data[0]["lon"]) 
    except: 
        raise RuntimeError(f"ѓ®а®¤ '{city}' ­Ґ ­ ©¤Ґ­") 
