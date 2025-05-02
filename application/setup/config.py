import os
from urllib.parse import quote_plus
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Config:
    USER    = os.environ.get("MONGODB_USERNAME")
    PWD     = os.environ.get("MONGODB_PASSWORD")
    HOST    = "custody.do58rxn.mongodb.net"
    DB_NAME = os.environ.get("MONGODB_DATABASE", "penitipan_hewan")

    # percent‑encode the password
    PWD_ENC = quote_plus(PWD)

    MONGO_URI = (
        f"mongodb+srv://{USER}:{PWD_ENC}@{HOST}/{DB_NAME}"
        "?retryWrites=true&w=majority&appName=Custody"
    )