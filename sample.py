"""
This file demonstrates an example of how to connect to a MongoDB database using the mongolib library.
It includes the following steps:
1. Connecting to a MongoDB instance using the provided connection string.
2. Creating a new database named 'Discord' if it does not already exist.
3. Creating a new collection named 'users' within the 'Discord' database if it does not already exist.
4. Inserting a user document into the 'users' collection with fields such as name, email, age, and phone_numbers.
The example uses asynchronous programming with the asyncio library to handle the database operations efficiently.
"""


import asyncio

import mongolib

async def main():
    client = mongolib.mongolib()
    await client.connect("mongodb://localhost:27017/")
    await client.create_db("Discord")
    await client.create_collection("Discord", "users")
    await client.create_user("Discord", "users", {
        "name": "John Doe",
        "email": "xxx@y.com",
        "age": 20,
        "phone_numbers": "1234567890",
    })
    

asyncio.run(main())