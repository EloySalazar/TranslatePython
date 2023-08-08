from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound

while True:
    idiom = input("Enter the language you want to translate: ")

    print("For example ""es"" is Spanish and ""en"" is English")

    text = input("Write what you want to translate: ")

    translator = GoogleTranslator(source='auto', target=idiom)
    traduc = translator.translate(text)

    tts = gTTS(traduc, lang='es-us', slow=True)
    
    print(traduc)

    tts.save("sound.mp3")

    playsound('sound.mp3')
