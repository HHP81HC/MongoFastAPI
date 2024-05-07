"""Create client engine"""
import motor.motor_asyncio


MONGODB_URL = "mongodb://192.168.1.10:27017/college?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.college
