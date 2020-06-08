import speech_recognition as srtwo
import RegisterFiles.students as st
a = srtwo.Recognizer()


class Registers():
    def __init__(self):
        with srtwo.Microphone() as source:
            print("Que registro desea realizar:")
            audio = a.listen(source)
            self.funcionsRegisters(audio)
    def funcionsRegisters(self, audio):
        text = a.recognize_google(audio)
        audio = format(text)
        print(audio)
        try:
            if(audio == "estudiante"):
                with srtwo.Microphone() as source:
                    print("Nombre del alumno:")
                    audio = a.listen(source)
                    audioName = a.recognize_google(audio)
                    audioName = format(audioName)
                    print(audioName)
                    with srtwo.Microphone() as source:
                        print("Apellido del alumno:")
                        audio= a.listen(source)
                        audioLastname = a.recognize_google(audio)
                        audioLastname = format(audioLastname)
                        print(audioLastname)
                        with srtwo.Microphone() as source:
                            print("Grupo del alumno:")
                            audio = a.listen(source)
                            audiogrup = a.recognize_google(audio)
                            audiogrup = format(audiogrup)
                            print(audiogrup)
                            with srtwo.Microphone() as source:
                                print("Carrera del alumno: ")
                                audio = a.listen(source)
                                audiocarrer = a.recognize_google(audio)
                                audiocarrer = format(audiocarrer)
                                print(audiocarrer)
                                with srtwo.Microphone() as source:
                                    print("Edad del alumno: ")
                                    audio = a.listen(source)
                                    audioage = a.recognize_google(audio)
                                    audioage = format(audioage)
                                    print(audioage)
                                    with srtwo.Microphone() as source:
                                        print("Id de la materia: ")
                                        audio = a.listen(source)
                                        audiosubject = a.recognize_google(audio)
                                        audiosubject = format(audiosubject)
                                        print(audiosubject)
                                        with srtwo.Microphone() as source:
                                            print("Nombre de la materia: ")
                                            audio=a.listen(source)
                                            audionamesubject = a.recognize_google(audio)
                                            audionamesubject = format(audionamesubject)
                                            print(audionamesubject)
                                            with srtwo.Microphone() as source:
                                                print("Horario de la matera")
                                                audio=a.listen(source)
                                                audioschedule = a.recognize_google(audio)
                                                audioschedule = format(audioschedule)
                                                print(audioschedule)
                                                if (audioschedule != ""):
                                                    st.students(audioName, audioLastname, audiogrup, audiocarrer,audioage, audiosubject,audionamesubject,audioschedule)
            else:
                print("No hay opciòn disponible")
                Registers()


        except srtwo.UnknownValueError:
            print("Could not understand audio")
        except srtwo.RequestError as e:
            print("Could not request results; {0}".format(e))