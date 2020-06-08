from RegisterFiles.MongoConnection.mongoConnection import connection

class students():
    def __init__(self, name, lastname, group, carrer, age, idSubject, subjectName, schedule):
        mc = connection()
        studentColection = mc.conex()["Students"]
        studentDocument = {
            "name": name,
            "lastname": lastname,
            "group": group,
            "carrer": carrer,
            "age": age,
            "subjects": {
                "idSubject": idSubject,
                "subjectName": subjectName,
                "schedule": schedule
            }
        }
        insert = studentColection.insert_one(studentDocument)
        print("Se inserto con exito con el id: ", insert.inserted_id)