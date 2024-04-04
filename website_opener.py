import webbrowser

def open_website(voice, website_name):
    websites = {
        'google': 'https://www.google.com',
        'youtube': 'https://www.youtube.com',
        'facebook': 'https://www.facebook.com',
        'вк': 'https://www.vk.com/',
        'яндекс': 'https://www.yandex.com/',
        'instagram': 'https://www.instagram.com',
        'twitter': 'https://twitter.com',
        'linkedin': 'https://www.linkedin.com',
        'reddit': 'https://www.reddit.com',
        'pinterest': 'https://www.pinterest.com',
        'amazon': 'https://www.amazon.com',
        'ebay': 'https://www.ebay.com',
        'netflix': 'https://www.netflix.com',
        'twitch': 'https://www.twitch.tv',
        'spotify': 'https://www.spotify.com',
        'discord': 'https://discord.com',
        'quora': 'https://www.quora.com',
        'medium': 'https://medium.com',
        'tumblr': 'https://www.tumblr.com',
        'flickr': 'https://www.flickr.com',
        'snapchat': 'https://www.snapchat.com',
        'whatsapp': 'https://www.whatsapp.com',
        'telegram': 'https://www.telegram.org',
        'slack': 'https://www.slack.com',
        'microsoft': 'https://www.microsoft.com',
        'apple': 'https://www.apple.com',
        'adobe': 'https://www.adobe.com',
        'github': 'https://github.com',
        'stackoverflow': 'https://stackoverflow.com',
        'wikipedia': 'https://www.wikipedia.org',
        'baidu': 'https://www.baidu.com',
        'aliexpress': 'https://www.aliexpress.com',
        'booking': 'https://www.booking.com',
        'airbnb': 'https://www.airbnb.com',
        'uber': 'https://www.uber.com',
        'zoom': 'https://zoom.us',
        'dropbox': 'https://www.dropbox.com',
        'salesforce': 'https://www.salesforce.com',
        'oracle': 'https://www.oracle.com',
        'sap': 'https://www.sap.com',
    }

    if website_name in websites:
        url = websites[website_name]
        webbrowser.open(url)
        voice.say(f'Открываю {website_name}')
        voice.runAndWait()
    else:
        voice.say('Извините, не могу открыть этот веб-сайт. Пожалуйста, попробуйте другой.')
        voice.runAndWait()

def search_in_web(query):
    url = 'https://www.google.com/search?q=' + '+'.join(query.split())
    webbrowser.open(url)