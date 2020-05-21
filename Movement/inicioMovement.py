import roby
import speech_recognition as sr
r = sr.Recognizer()

class Movements():
    def __init__(self):
        with sr.Microphone() as source:
            print("Que movimiento desea realizar:")
            audio = r.listen(source)
            self.funcionsMovements(audio)

    def funcionsMovements(self, audio):
        if(audio == "Acelera"):
            roby.arranca()
        elif audio == "derecha":
            roby.right()
        elif audio == "izquierda":
            roby.left()
