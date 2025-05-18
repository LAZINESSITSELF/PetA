from pymongo import MongoClient
from pymongo.server_api import ServerApi

db = None

def init_db(app):
    global db
    uri = app.config['MONGO_URI']
    client = MongoClient(uri, server_api=ServerApi("1"))
    db = client[app.config.get('DB_NAME', 'penitipan_hewan')]
    app.db = db

    try:
        client.admin.command("ping")
        print("MongoDB connected successfully!")
    except Exception as e:
        print("MongoDB connection error:", e)