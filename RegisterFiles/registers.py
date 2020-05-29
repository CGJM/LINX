#import roby
import speech_recognition as sr
#from students import students
r = sr.Recognizer()


class Registers():
    def __init__(self):
        with sr.Microphone() as source:
            print("Que registro desea realizar:")
            audio = r.listen(source)
            self.funcionsRegisters(audio)
    def funcionsRegisters(self, audio):
        text = r.recognize_google(audio)
        audio = format(text)
        try:
            if(audio == "estudiante"):
                with sr.Microphone() as source:
                    print("Nombre del alumno:")
                    audioName = r.listen(source)
                    if(audioName != ""):
                        print("Apellido del alumno:")
                        audioLastname= r.listen(source)
                        if (audioLastname != ""):
                            print("Grupo del alumno:")
                            audiogrup = r.listen(source)
                            if (audiogrup != ""):
                                print("Edad del alumno")
                                audioage = r.listen(source)
                                if (audioage != ""):
                                    print("Id de la materia")
                                    audiosubject = r.listen(source)
                                    print("Hola: ",audioName)
            else:
                print("Hola")


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

Registers()