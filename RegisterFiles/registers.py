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
        print(audio)
        try:
            if(audio == "estudiante"):
                with sr.Microphone() as source:
                    print("Nombre del alumno:")
                    audio = r.listen(source)
                    audioName = r.recognize_google(audio)
                    audioName = format(audioName)
                    print("Apellido del alumno:")
                    audio= r.listen(source)
                    audioLastname = r.recognize_google(audio)
                    audioLastname = format(audioLastname)
                    print(audioLastname+ "" + audioName)
                    print("Grupo del alumno:")
                    audio = r.listen(source)
                    audiogrup = r.recognize_google(audio)
                    audiogrup = format(audiogrup)
                    print("Carrera del alumno: ")
                    audio = r.listen(source)
                    audiocarrer = r.recognize_google(audio)
                    audiocarrer = format(audiocarrer)
                    print("Edad del alumno: ")
                    audio = r.listen(source)
                    audioage = r.recognize_google(audio)
                    audioage = format(audioage)
                    print("Id de la materia: ")
                    audio = r.listen(source)
                    audiosubject = r.recognize_google(audio)
                    audiosubject = format(audiosubject)
                    print("Nombre de la materia: ")
                    audio=r.listen(source)
                    audionamesubject = r.recognize_google(audio)
                    audionamesubject = format(audionamesubject)
                    print("Horario de la matera")
                    audio=r.listen(source)
                    audioschedule = r.recognize_google(audio)
                    audioschedule = format(audioschedule)
                    st(audioName, audioLastname, audiogrup, audiocarrer,audioage, audiosubject,audionamesubject,audioschedule)
                                        #print("Hola: ",audioName)
            else:
                print("No hay opciòn disponible")
                Registers()


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

#Registers()
