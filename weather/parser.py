WEATHER_CODES = { 
    0: "Ясно", 1: "Преимущественно ясно", 2: "Переменная облачность", 
    3: "Пасмурно", 45: "Туман", 48: "Иней", 61: "Небольшой дождь", 
    63: "Дождь", 65: "Ливень", 71: "Небольшой снег", 73: "Снег", 
    95: "Гроза", } 
 
def print_weather(data: dict, place: str): 
    desc = WEATHER_CODES.get(data["code"], "Неизвестно") 
    print("\n" + "="*50) 
    print(f"   Погода: {place}") 
    print(f"   Температура: {data['temp']}{data['unit']}") 
    print(f"       Состояние: {desc}") 
    print(f"           Ветер: {data['wind']} м/с") 
    print("="*50 + "\n") 
