import requests 
from .cache import get_cache, set_cache 
 
def get_weather(lat: float, lon: float, unit="celsius"): 
    key = f"{lat}_{lon}_{unit}" 
    cached = get_cache(key) 
    if cached: return cached 
 
    url = "https://api.open-meteo.com/v1/forecast" 
    params = { 
        "latitude": lat, "longitude": lon, 
        "current_weather": True, 
        "temperature_unit": "fahrenheit" if unit=="fahrenheit" else "celsius", 
        "windspeed_unit": "ms", "timezone": "auto" } 
 
    try: 
        r = requests.get(url, params=params, timeout=10) 
        r.raise_for_status() 
        data = r.json()["current_weather"] 
        result = { 
            "temp": data["temperature"], 
            "wind": data["windspeed"], 
            "code": data["weathercode"], 
            "unit": "шF" if unit=="fahrenheit" else "шC" } 
        set_cache(key, result) 
        return result 
    except Exception as e: 
        raise RuntimeError(f"API error: {e}") 
