from pymongo import MongoClient

URL = "mongodb://localhost:27017/"
DATABASE = "bancoiot"


class Database:
    def __init__(self) -> None:
        self.connect()

    def connect(self) -> None:
        try:
            self.client = MongoClient(URL)
            self.db = self.client[DATABASE]
            print("Conectado ao banco de dados")
        except Exception as e:
            print("Erro ao conectar ao banco de dados")
            print(e)

    def get_collection(self, collection):
        if collection in self.db.list_collection_names():
            return self.db[collection]
        else:
            return self.createCollectionIfNotExists(collection)

    def createCollectionIfNotExists(self, collection_name, validator=None):
        # if collection_name already exists, update the validator and return the collection
        if collection_name in self.db.list_collection_names():
            # update validation schema
            self.db.command(
                "collMod",
                collection_name,
                validator=validator,
                validationAction="error"
            )
            return self.db[collection_name]
        else:
            return self.db.create_collection(collection_name, validator=validator)
