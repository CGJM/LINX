import speech_recognition as sr
import RegisterFiles.students as st
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
                                print("Carrera del alumno")
                                audiocarrer = r.listen(source)
                                if (audiocarrer != ""):
                                    print("Edad del alumno")
                                    audioage = r.listen(source)
                                    if (audioage != ""):
                                        print("Id de la materia")
                                        audiosubject = r.listen(source)
                                        if(audiosubject != ""):
                                            print("Nombre de la matera")
                                            audionamesubject=r.listen(source)
                                            if(audionamesubject != ""):
                                                print("Horario de la matera")
                                                audioschedule=r.listen(source)
                                                st(audioName, audioLastname, audiogrup, audiocarrer,audioage, audiosubject,audionamesubject,audioschedule)
                                        print("Hola: ",audioName)
            else:
                print("No hay opciòn disponible")


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

Registers()
