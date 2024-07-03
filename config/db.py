from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://udaiveersetia:udayveir@cluster0.vxcducw.mongodb.net/notes"

conn = MongoClient(MONGO_URI,tlsCAFile=certifi.where())