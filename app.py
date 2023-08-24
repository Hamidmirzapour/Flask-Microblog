from flask import Flask, render_template, request
from datetime import datetime
from pymongo import MongoClient

app = Flask("__name__")
client = MongoClient("mongodb+srv://hamid:H_amid16021996@cluster0.ovzbjxx.mongodb.net/")
app.db = client.microblog

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content_entry = request.form.get("content")
        today = datetime.today().strftime("%m/%d/%Y")
        app.db.entries.insert_one({"content": content_entry, "date": today})
    entries = [
        (
            entry["content"],
            entry["date"],
            datetime.strptime(entry["date"], "%m/%d/%Y").strftime("%b %d")
        )
        for entry in app.db.entries.find({})]
    return render_template("index.html", entries=entries)