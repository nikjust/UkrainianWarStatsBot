from datetime import datetime
import json
import requests

def today():
       now = datetime.now()
       date_time = now.strftime("%d_%m_20%y")
       print("date:", date_time)
       print(info_day(date_time))
       return info_day(date_time)

def info_day(day: str):
       try:
              json_info = requests.get(f'https://opermap.mash.ru/json/{day}.json')
              info = json.loads(json_info.text)
              russia_captured_cities = info["captured"]
              hotspots = info["hotspots"]

              newline = "\n▪️ "



              text = f"*🏘Захваченные Россией города🏘*: {' '.join(str(city[0].capitalize() + city[1:]+', ') for city in russia_captured_cities)[0:-2]+'.'}" \
                     "\n*🔔События🔔*:\n▪️ " \
                     f"{newline.join(str(hotspot['title']) for hotspot in hotspots)}"
              return text
       except Exception as e:
              return f"Ошибка :( -> \n {e}"
