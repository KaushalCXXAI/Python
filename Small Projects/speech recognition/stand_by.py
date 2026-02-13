import speech_recognition as sr
speech = sr.Recognizer()

while True:

    print("Speak Anything :")
    input = ""
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            pass
        except sr.WaitTimeoutError:
            pass

    if input == "stop listening now":
        break

    print("You said : {}".format(input))