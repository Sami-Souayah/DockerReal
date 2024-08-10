from pymongo import MongoClient
def get_database():
    CONNECTION_STRING = "mongodb+srv://souays:sami2003@cdccluster0.7gs5p.mongodb.net/"
    client = MongoClient(CONNECTION_STRING)
    return client["Vaccines"]

if __name__=="__main__":
    dbname = get_database()

#new connection string mongodb+srv://souays:sami2003@cdccluster0.7gs5p.mongodb.net/


