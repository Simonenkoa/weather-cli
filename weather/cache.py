import json 
import os 
from datetime import datetime, timedelta 
 
CACHE_DIR = "cache" 
CACHE_TIME = timedelta(minutes=10) 
os.makedirs(CACHE_DIR, exist_ok=True) 
 
def get_cache(key: str): 
    file = f"{CACHE_DIR\{key}.json" 
    if not os.path.exists(file): return None 
    try: 
        with open(file, encoding="utf-8") as f: 
            data = json.load(f) 
            ts = datetime.fromisoformat(data["time"]) 
            if datetime.now() - ts < CACHE_TIME: return data["data"] 
    except: pass 
    return None 
 
def set_cache(key: str, data: dict): 
    try: 
        with open(f"{CACHE_DIR}\{key}.json", "w", encoding="utf-8") as f: 
            json.dump({"time": datetime.now().isoformat(), "data": data}, f, ensure_ascii=False, indent=2) 
    except Exception as e: print("νθ ®θ¨΅ª :", e) 
