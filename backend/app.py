from flask import Flask, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://notesstack_mongo:27017")
client = MongoClient(MONGO_URI)
db = client['notesdb']
notes_col = db['notes']

DEFAULT_NOTE = {
    "title": "Hello from the backend this data is coming from MongoDB"
}

def serialize(note):
    return {
        "_id": str(note.get("_id")),
        "title": note.get("title")
    }

@app.route("/note", methods=["GET"])
def get_note():
    note = notes_col.find_one()
    if not note:
        insert_note = notes_col.insert_one(DEFAULT_NOTE.copy())
        note = notes_col.find_one({"_id": insert_note.inserted_id})
        print(note)
    return jsonify(serialize(note))

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
