import speech_recognition as sr
import Movement.inicioMovement as mv
import RegisterFiles.registers as re
r = sr.Recognizer()
def inicio():
    with sr.Microphone() as source:
        print("Hola, que desea realizar:")
        audio = r.listen(source)
        funciones(audio)

def funciones(audio):
#    aud=re()
    try:
        aud= r.recognize_google(audio)
        audio= format(aud)
        print("Tu opción fue: " + audio)
        if audio == 'move':
            print('hello ')
            mv.Movements()
        elif audio == 'registro':
            print('Registro')
            re.Registers()
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))



inicio()
