import argparse 
from weather.utils import city_to_coords 
from weather.api import get_weather 
from weather.parser import print_weather 
 
parser = argparse.ArgumentParser(description="Џ®Ј®¤  ў вҐа¬Ё­ «Ґ") 
group = parser.add_mutually_exclusive_group(required=True) 
group.add_argument("--city", help="Ќ §ў ­ЁҐ Ј®а®¤ ") 
group.add_argument("--lat", type=float, help="Ёа®в ") 
group.add_argument("--lon", type=float, help="„®«Ј®в ") 
parser.add_argument("--unit", choices=["celsius","fahrenheit"], default="celsius") 
args = parser.parse_args() 
 
try: 
    if args.city: 
        print(f"€йҐ¬ {args.city}...") 
        lat, lon = city_to_coords(args.city) 
        place = args.city.capitalize() 
    else: 
        lat, lon = args.lat, args.lon 
        place = f"({lat}, {lon})" 
    weather = get_weather(lat, lon, args.unit) 
    print_weather(weather, place) 
except Exception as e: 
    print(f"ЋиЁЎЄ : {e}") 

