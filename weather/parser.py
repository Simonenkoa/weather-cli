WEATHER_CODES = { 
    0: "џб­®", 1: "ЏаҐЁ¬гйҐбвўҐ­­® пб­®", 2: "ЏҐаҐ¬Ґ­­ п ®Ў« з­®бвм", 
    3: "Џ б¬га­®", 45: "’г¬ ­", 48: "€­Ґ©", 61: "ЌҐЎ®«ми®© ¤®¦¤м", 
    63: "„®¦¤м", 65: "‹ЁўҐ­м", 71: "ЌҐЎ®«ми®© б­ҐЈ", 73: "‘­ҐЈ", 
    95: "ѓа®§ ", } 
 
def print_weather(data: dict, place: str): 
    desc = WEATHER_CODES.get(data["code"], "ЌҐЁ§ўҐбв­®") 
    print("\n" + "="*50) 
    print(f"   Џ®Ј®¤ : {place}") 
    print(f"   ’Ґ¬ЇҐа вга : {data['temp']}{data['unit']}") 
    print(f"       ‘®бв®п­ЁҐ: {desc}") 
    print(f"           ‚ҐвҐа: {data['wind']} ¬/б") 
    print("="*50 + "\n") 
