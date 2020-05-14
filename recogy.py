import speech_recognition as sr
#import robby
r = sr.Recognizer()
def inicio():
    with sr.Microphone() as source:
        print("Di algo:")
        audio = r.listen(source)
        funciones(audio)

def funciones(audio):
    try:
        print("Dijiste " + r.recognize_google(audio))
        if r.recognize_google(audio)=='hello':
            print('hello ')
            #robby.arranca()
            #inicio()
        elif r.recognize_google(audio)=='stop':
            robby.stop()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



inicio()