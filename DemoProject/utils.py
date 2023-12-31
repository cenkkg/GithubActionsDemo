import requests
from bs4 import BeautifulSoup
import json
import os


bgs = {
        "overcast clouds": "static/images/clouds.jpeg",
        "clear sky": "static/images/clear.jpeg",
        "snow": "static/images/snow.jpeg",
        "heavy intensity rain": "static/images/heavyrain.jpeg",
        "moderate rain": "static/images/rain.jpeg",
        "light intensity shower rain": "static/images/rain.jpeg",
        "broken clouds": "static/images/brokenclouds.jpeg",
        "scattered clouds": "static/images/scatteredclouds.jpeg",
        "few clouds": "static/images/fewclouds.jpeg",
        "light rain": "static/images/lightrain.jpeg",
        "light intensity drizzle": "static/images/lightrain.jpeg",
        "haze": "static/images/haze.jpeg",
        "fog": "static/images/fog.jpeg",
        "default": "static/images/default.jpeg",
    }


api = {
    "key": "f738629a362bfb615e811eeeda4f40a1",
    "baseurl": "https://api.openweathermap.org/data/2.5/",
    "city": "phuket"
}

url = "http://localhost:3000"


def get_daily_data():
    data = f"{api['baseurl']}/weather?q={api['city']}&units=metric&APPID={api['key']}"
    response = requests.get(data)
    return response.json()


def get_weekly_data():
    city = get_daily_data()
    days = f"{api['baseurl']}onecall?lat={city['coord']['lat']}&lon={city['coord']['lon']}&units=metric&appid={api['key']}"
    response = requests.get(days)
    return response.json()['daily']


def save_search_history(city, date, time):
    data_dict = {
        "city": city,
        "date": date,
        "time": time,
    }

    json_file = 'history.json'
    if not os.path.exists(json_file):
        with open(json_file, "w") as file:
            file.write('[]')
            
    with open(json_file, "r+") as file:
        data = json.load(file)
        data.append(data_dict)
        file.seek(0)
        json.dump(data, file, indent=4)

    
def is_url_up(url):
    try:
        r = requests.head(url)
    except Exception:
        return False
    return r.status_code == 200


def is_website_running(url):
    try:
        r = requests.get(url)
        title = BeautifulSoup(r.text, 'html.parser')
    except Exception:
        return False
    return title.find("title").get_text()
