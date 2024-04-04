import threading

timer = None

def timer_expired(voice):
    voice.say("Время истекло")
    voice.runAndWait()

def set_timer(voice, hours, minutes):
    global timer
    total_minutes = hours * 60 + minutes
    voice.say(f"Таймер на {hours} часов {minutes} минут установлен")
    timer = threading.Timer(total_minutes * 60, timer_expired, args=(voice,))
    timer.start()

def cancel_timer(voice):
    global timer
    if timer:
        timer.cancel()
        voice.say("Таймер отменен")
        voice.runAndWait()
    else:
        voice.say("Нет активного таймера для отмены")
        voice.runAndWait()


