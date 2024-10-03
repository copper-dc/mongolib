from pymongo import MongoClient

class mongolib:

    async def connect(self, connectionstring: str):
        self.client = AsyncIOMotorClient(connectionstring)
        print("Connected to MongoDB")