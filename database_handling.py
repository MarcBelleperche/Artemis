# Still an idea, i don't even know if i will keep it ... a local Json might be enough

import pymongo


def init_database(port, dico):
    try:
        db = pymongo.MongoClient('localhost', port)
        print("Successfully connect Mongo")
        artemis_db = db.Artemis_MARK1
        print("Successfully connect the database Artemis_Mark1")
    except:
        print("Connection failed ...")

    initial_insert = artemis_db.basicinfos
    iain = {
        "IAName": "Artemis"
    }
    initial_insert.insert_one(iain)

#def get_value_from_db
