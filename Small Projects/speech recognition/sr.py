import speech_recognition as sr

speech = sr.Recognizer()
print("Speak Anything :")
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    input = speech.recognize_google(audio)
    print("You said : {}".format(input))
