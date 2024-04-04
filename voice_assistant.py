from folderes import create_folder, delete_folder, rename_folder, list_files, copy_files, search_files
from timer_functions import set_timer, cancel_timer
from website_opener import open_website, search_in_web
from weather_forecast import get_weather_forecast
from translate import translate_with_voice_assistant
from ai_1 import main
import speech_recognition as sr
import pyttsx3
import random
import datetime
import time

is_timer_running = False
start_time = 0
recognizer = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я твой голосовой помощник!')
voice.runAndWait()
list_hi = ['привет','здраствуйте','хэй','hello','добрый день']
list_bye = ['пока', 'до свидания', 'до встречи', 'хорошего дня', 'good bye', 'bye']

while True:
    with sr.Microphone(device_index=0) as sourse:
        recognizer.adjust_for_ambient_noise(sourse, duration=3)
        print('Скажи что-нибудь...')
        audio = recognizer.listen(sourse)

    try:
        speech = recognizer.recognize_google(audio, language='ru_RU').lower()
        print('Вы сказали: ' + speech)

        for greeting in list_hi:
            if greeting in speech:
                voice.say(random.choice(list_hi))
                voice.runAndWait()

        if speech.find('текущее время') >= 0:
            current_time = datetime.datetime.now().strftime("%H:%M")
            voice.say("Текущее время: " + current_time)
            voice.runAndWait()

        elif speech.find('поставь таймер на') >= 0:
            if "час" in speech or "минут" in speech:
                time_str = speech.split("поставь таймер на ")[1]
                words = time_str.split()
                hours = 0
                minutes = 0
                if "час" in words:
                    index = words.index("час")
                    hours = int(words[index - 1])
                if "минут" in words:
                    index = words.index("минут")
                    minutes = int(words[index - 1])

                set_timer(voice, hours, minutes)

            else:
                voice.say("Некорректное время. Пожалуйста, введите время в формате часы час/минуты минуты.")
            voice.runAndWait()

        elif speech.find('отмени таймер') >= 0 or speech.find('удали таймер') >= 0:
            cancel_timer(voice)
            voice.runAndWait()

        elif speech.find('запусти секундомер') >= 0:
            if not is_timer_running:
                voice.say("Секундомер запущен")
                start_time = time.time()
                is_timer_running = True
            else:
                voice.say("Секундомер уже запущен")
            voice.runAndWait()

        elif speech.find('останови секундомер') >= 0:
            if is_timer_running:
                elapsed_time = time.time() - start_time
                voice.say(f"Секундомер остановлен. Прошло {int(elapsed_time)} секунд")
                is_timer_running = False
            else:
                voice.say("Секундомер не был запущен")
            voice.runAndWait()

        elif speech.find('сколько прошло секунд') >= 0:
            if is_timer_running:
                elapsed_time = time.time() - start_time
                voice.say(f"Секундомер уже запущен. Прошло {int(elapsed_time)} секунд")
            else:
                voice.say("Секундомер не был запущен")
            voice.runAndWait()

        elif speech.find('создай папку') >= 0:
            name_folder = speech.split('создай папку ')[1]
            new_folder = create_folder(name_folder)
            voice.say(new_folder)
            voice.runAndWait()

        elif speech.find('удали папку') >= 0:
            name_folder = speech.split('удали папку ')[1]
            new_folder = delete_folder(name_folder)
            voice.say(new_folder)
            voice.runAndWait()

        elif 'переименуй папку' in speech:
            old_name = speech.split('переименуй папку ')[1].split(' на ')[0]
            new_name = speech.split(' на ')[1]
            new_folder = rename_folder(old_name, new_name)
            voice.say(new_folder)
            voice.runAndWait()

        elif speech.find('покажи содержимое папки') >= 0:
            name_folder = speech.split('покажи содержимое папки ')[1]
            new_folder = list_files(name_folder)
            voice.say(new_folder)
            voice.runAndWait()

        elif speech.find('скопируй файлы') >= 0:
            src_folder = speech.split('скопируй файлы из ')[1].split(' в ')[0]
            dest_folder = speech.split(' в ')[1]
            new_folder = copy_files(src_folder, dest_folder)
            voice.say(new_folder)
            voice.runAndWait()

        elif speech.find('найди слово') >= 0:
            keyword = speech.split('найди слово ')[1].split(' в папке ')[0]
            folder_name = speech.split(' в папке ')[1]
            new_folder = search_files(folder_name, keyword)
            voice.say(new_folder)
            voice.runAndWait()

        elif speech.find('открой') >= 0:
            website_name = speech.split('открой ')[1]
            open_website(voice, website_name)

        elif speech.find('прогноз погоды в') >= 0:
            city = speech.split('прогноз погоды в ')[1]
            forecast = get_weather_forecast(city)
            print(forecast)
            voice.say(forecast)
            voice.runAndWait()

        elif speech.find('поиск в интернете') >= 0:
            query = speech.split('поиск в интернете ')[1]
            weber = search_in_web(query)
            voice.say(weber)
            voice.runAndWait()

        elif speech.find('переведи') >= 0:
            text_to_translate = speech.split('переведи ')[1].split(' на ')[0]
            language = speech.split('на ')[1]
            translated_text = translate_with_voice_assistant(text_to_translate, language)
            print(translated_text)
            voice.say(translated_text)
            voice.runAndWait()

        elif speech.find('нейросеть') >= 0:
            main()
            voice.runAndWait()

        else:
            voice.say('Я вас не понимаю')
            voice.runAndWait()

        for greeping in list_bye:
            if greeping in speech:
                voice.say(random.choice(list_bye))
            voice.runAndWait()
            break

    except sr.UnknownValueError:\
        voice.say("Google Speech Recognition не смог распознать аудио.")
    except sr.RequestError as e:\
        voice.say("Не удалось отправить запрос на распознавание речи; {0}".format(e))