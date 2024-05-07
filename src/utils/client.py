"""Create client engine"""
import motor.motor_asyncio


MONGODB_URL = "mongodb://localhost:27017/college?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.college
