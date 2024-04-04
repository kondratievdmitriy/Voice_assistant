import openai
import speech_recognition as sr
import pyttsx3

# Инициализация клиента OpenAI с вашим API ключом
client = openai.Client(api_key="your api key",
                       base_url="https://api.proxyapi.ru/openai/v1")

engine = pyttsx3.init()

# Инициализация списка сообщений для поддержания контекста разговора
def chat_with_ai(user_message):
    messages = [{"role": "user", "content": user_message}]

    # Посылаем запрос к нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )

    # Получаем ответ от нейросети
    response_message = chat_completion.choices[0].message.content

    print("AI:", response_message)
    engine.say(response_message)
    engine.runAndWait()

# Функция для распознавания речи пользователя
def get_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Говорите что-нибудь:")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        return text
    except sr.UnknownValueError:
        return "Не удалось распознать речь"
    except sr.RequestError:
        return "Ошибка при отправке запроса к службе распознавания речи"

# Главная функция для взаимодействия с голосовым помощником
def main():
    initial_message = "Привет, чем я могу тебе помочь?"
    chat_with_ai(initial_message)

    while True:
        user_message = get_audio()
        if "стоп" in user_message.lower():
            break
        chat_with_ai(user_message)
