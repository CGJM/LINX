import pymongo

class connection():

    def conex(self ):
        mongodb = pymongo.MongoClient("mongodb://localhost:27017/")
        mydatabase = mongodb["Linx"]
        return mydatabase