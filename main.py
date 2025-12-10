import argparse 
from weather.utils import city_to_coords 
from weather.api import get_weather 
from weather.parser import print_weather 
 
parser = argparse.ArgumentParser(description="Погода в терминале") 
group = parser.add_mutually_exclusive_group(required=True) 
group.add_argument("--city", help="Название города") 
group.add_argument("--lat", type=float, help="Широта") 
group.add_argument("--lon", type=float, help="Долгота") 
parser.add_argument("--unit", choices=["celsius","fahrenheit"], default="celsius") 
args = parser.parse_args() 
 
try: 
    if args.city: 
        print(f"Ищем {args.city}...") 
        lat, lon = city_to_coords(args.city) 
        place = args.city.capitalize() 
    else: 
        lat, lon = args.lat, args.lon 
        place = f"({lat}, {lon})" 
    weather = get_weather(lat, lon, args.unit) 
    print_weather(weather, place) 
except Exception as e: 
    print(f"Ошибка: {e}") 
