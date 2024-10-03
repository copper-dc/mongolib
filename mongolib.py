from motor.motor_asyncio import AsyncIOMotorClient

class mongolib:
    def __init__(self):
        self.client = None

    async def connect(self, connection_string: str):
        self.client = AsyncIOMotorClient(connection_string)
        print("Connected to MongoDB")
        return self.client

    async def create_db(self, database_name: str):
        db = self.client[database_name]
        print(f"{database_name} Database Created")
        return db

    async def create_collection(self, database_name: str, collection_name: str):
        db = self.client[database_name]
        collection = db[collection_name]
        print(f"{collection_name} Collection Created in {database_name} Database")
        return collection

    async def create_user(self, database_name: str, collection_name: str, data: dict):
        """
        The `data` parameter is a dictionary that contains the user information to be stored in MongoDB.
        Example of `data` dictionary:
        
        data = {
            "name": "xxx yyy",
            "email": "xxx.yyy@example.com",
            "age": xy,
            "phone_numbers":"1234567890",
            "created_at": datetime.datetime.utcnow(),
            "last_active": datetime.datetime.utcnow(),
        }
        
        This dictionary can contain any fields you need to store for a user.
        The `insert_one` method will insert this document into the specified collection in MongoDB.
        """
        db = self.client[database_name]
        collection = db[collection_name]
        result = await collection.insert_one(data)
        print(f"User Created with ID: {result.inserted_id} in {collection_name} Collection at {database_name}")

    async def get_user(self, database_name: str, collection_name: str, query: dict):
        """
        Asynchronously retrieves a user document from a specified MongoDB collection.

        Args:
            database_name (str): The name of the database to query.
            collection_name (str): The name of the collection to query.
            query (dict): The query dictionary to filter the user document.

        Returns:
            dict: The user document found in the collection, or None if no document matches the query.

        Example:
            result = await get_user("Discord", "users", {"username": "johndoe"})
            if result:
                print("User found:", result)
            else:
                print("User not found.")
        """
        db = self.client[database_name]
        collection = db[collection_name]
        result = await collection.find_one(query)
        print(f"User Found: {result} in {collection_name} Collection at {database_name}")
        return result
