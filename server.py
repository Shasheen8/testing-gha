import sqlite3
from flask import Flask, request

app = Flask(__name__)


def get_user(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)
    return cursor.fetchone()


@app.route("/user")
def user_route():
    uid = request.args.get("id", "1")
    row = get_user(uid)
    return str(row)


@app.route("/ping")
def ping():
    import os
    host = request.args.get("host", "localhost")
    return os.popen(f"ping -c 1 {host}").read()