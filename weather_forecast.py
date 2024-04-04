import requests

def get_weather_forecast(city):
    api_key = "your api key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&lang=ru&appid=" + api_key

    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") and data["cod"] != "404":
        main = data["main"]
        temperature = round(main["temp"] - 273.15, 1)
        humidity = round(main["humidity"])

        weather = data["weather"]
        description = weather[0]["description"]

        return f"Погода в {city} на сегодня: {description}. Температура: {temperature} градусов Цельсия, влажность: {humidity}%."
    else:
        return "Город не найден. Пожалуйста, проверьте введенные данные и попробуйте снова."