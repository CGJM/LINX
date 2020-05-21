import speech_recognition as sr
#import robby
import Movement.inicioMovement
r = sr.Recognizer()
def inicio():
    with sr.Microphone() as source:
        print("Hola, que desea realizar:")
        audio = r.listen(source)
        funciones(audio)

def funciones(audio):
    try:
        print("Tu opción fue: " + r.recognize_google(audio))
        if r.recognize_google(audio) == 'Movimiento':
            print('hello ')
            #robby.arranca()
            #inicio()
        elif r.recognize_google(audio) == 'registro':
            print('Registro')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



inicio()