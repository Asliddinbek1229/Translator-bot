from googletrans import Translator

def translate(msg):
    translator = Translator()
    til = translator.detect(msg).lang
    if til == 'en':
        return translator.translate(msg, dest='uz').text
    else:
        return translator.translate(msg, dest='en').text