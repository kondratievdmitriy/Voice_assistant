import requests
API_KEY = 'your api key'
def translate(text, target_language):
    url = "https://translation.googleapis.com/language/translate/v2"
    params = {
        "key": API_KEY,
        "q": text,
        "target": target_language
    }
    response = requests.post(url, params=params)
    return response.json()["data"]["translations"][0]["translatedText"]

def translate_with_voice_assistant(text_to_translate, language):
    if language == 'китайский традиционный' or language == 'китайский':
        target_language = "zh-tw"
    elif language == 'китайский упрощенный':
        target_language = "zh-cn"
    elif language == 'английский':
        target_language = "en"
    elif language == 'французский':
        target_language = "fr"
    elif language == 'испанский':
        target_language = "es"
    elif language == 'японский':
        target_language = "ja"
    elif language == 'немецкий' or language == 'германский':
        target_language = "de"
    elif language == 'русский':
        target_language = "ru"
    elif language == 'эсперанто':
        target_language = "eo"
    elif language == 'хинди':
        target_language = "hi"
    elif language == 'итальянский':
        target_language = "it"
    elif language == 'казахский':
        target_language = "kk"
    elif language == 'африкаас' or language == 'африканский':
        target_language = "af"
    elif language == 'албанский':
        target_language = "sq"
    elif language == 'амхарский':
        target_language = "am"
    elif language == 'арабский':
        target_language = "ar"
    elif language == 'армянский':
        target_language = "hy"
    elif language == 'азербайджанский':
        target_language = "az"
    elif language == 'баскский':
        target_language = "eu"
    elif language == 'белорусский':
        target_language = "be"
    elif language == 'бенгальский':
        target_language = "bn"
    elif language == 'боснийский':
        target_language = "bs"
    elif language == 'болгарский':
        target_language = "bg"
    elif language == 'каталонский':
        target_language = "ca"
    elif language == 'кебуано':
        target_language = "ceb"
    elif language == 'чичева':
        target_language = "ny"
    elif language == 'корсиканский':
        target_language = "co"
    elif language == 'хорватский':
        target_language = "hr"
    elif language == 'чешский':
        target_language = "cs"
    elif language == 'датский':
        target_language = "da"
    elif language == 'голландский':
        target_language = "nl"
    elif language == 'эстонский':
        target_language = "et"
    elif language == 'филиппинский':
        target_language = "tl"
    elif language == 'финский':
        target_language = "fi"
    elif language == 'фризский':
        target_language = "fy"
    elif language == 'галисийский':
        target_language = "gl"
    elif language == 'грузинский':
        target_language = "ka"
    elif language == 'греческий':
        target_language = "el"
    elif language == 'гуджарати':
        target_language = "gu"
    elif language == 'гаитянский креольский':
        target_language = "ht"
    elif language == 'хауса':
        target_language = "ha"
    elif language == 'гавайский':
        target_language = "haw"
    elif language == 'иврит':
        target_language = "iw"
    elif language == 'хмонг':
        target_language = "hmn"
    elif language == 'венгерский':
        target_language = "hu"
    elif language == 'исландский':
        target_language = "is"
    elif language == 'лгбо' or language == 'ЛГБО':
        target_language = "ig"
    elif language == 'индонезийский':
        target_language = "id"
    elif language == 'ирландский':
        target_language = "ga"
    elif language == 'яванский':
        target_language = "jw"
    elif language == 'каннада' or language == 'каннадский':
        target_language = "kn"
    elif language == 'кхмерский':
        target_language = "km"
    elif language == 'корейский':
        target_language = "ko"
    elif language == 'курманджи' or language == 'курдский':
        target_language = "ku"
    elif language == 'кыргызский':
        target_language = "ky"
    elif language == 'лаосский':
        target_language = "lo"
    elif language == 'латинский':
        target_language = "la"
    elif language == 'латышский':
        target_language = "lv"
    elif language == 'литовский':
        target_language = "lt"
    elif language == 'люксембургский':
        target_language = "lb"
    elif language == 'македонский':
        target_language = "mk"
    elif language == 'малагасийский':
        target_language = "mg"
    elif language == 'малайский':
        target_language = "ms"
    elif language == 'малаялам':
        target_language = "ml"
    elif language == 'мальтийский':
        target_language = "mt"
    elif language == 'маори':
        target_language = "mi"
    elif language == 'маратхи':
        target_language = "mr"
    elif language == 'монгольский':
        target_language = "mn"
    elif language == 'мьянма' or language == 'бирманский':
        target_language = "my"
    elif language == 'непальский':
        target_language = "ne"
    elif language == 'норвежский':
        target_language = "no"
    elif language == 'одиа':
        target_language = "or"
    elif language == 'пушту':
        target_language = "ps"
    elif language == 'персидский':
        target_language = "fa"
    elif language == 'польский':
        target_language = "pl"
    elif language == 'португальский':
        target_language = "pt"
    elif language == 'панджаби':
        target_language = "pa"
    elif language == 'румынский':
        target_language = "ro"
    elif language == 'самоанский':
        target_language = "sm"
    elif language == 'шотландский гэльский' or language == 'гэльский' or language == 'шотландский':
        target_language = "gd"
    elif language == 'сербский':
        target_language = "sr"
    elif language == 'сесото':
        target_language = "st"
    elif language == 'шона':
        target_language = "sn"
    elif language == 'синдхи':
        target_language = "sd"
    elif language == 'сингальский':
        target_language = "si"
    elif language == 'словацкий':
        target_language = "sk"
    elif language == 'словенский':
        target_language = "sl"
    elif language == 'сомалийский':
        target_language = "so"
    elif language == 'суданский':
        target_language = "su"
    elif language == 'суахили':
        target_language = "sw"
    elif language == 'шведский':
        target_language = "sv"
    elif language == 'таджикский':
        target_language = "tg"
    elif language == 'тамильский':
        target_language = "ta"
    elif language == 'телугу':
        target_language = "te"
    elif language == 'тайский':
        target_language = "th"
    elif language == 'турецкий':
        target_language = "tr"
    elif language == 'украинский':
        target_language = "uk"
    elif language == 'урду':
        target_language = "ur"
    elif language == 'уйгурский':
        target_language = "ug"
    elif language == 'узбекский':
        target_language = "uz"
    elif language == 'вьетнамский':
        target_language = "vi"
    elif language == 'валлийский':
        target_language = "cy"
    elif language == 'коса':
        target_language = "xh"
    elif language == 'идиш':
        target_language = "yi"
    elif language == 'йоруба':
        target_language = "yo"
    elif language == 'зулу':
        target_language = "zu"
    else:
        print("Извините, я не знаю данный язык. Попробуйте повторить ваш запрос позже.")
        target_language = "ru"
    translated_text = translate(text_to_translate, target_language)
    return translated_text
