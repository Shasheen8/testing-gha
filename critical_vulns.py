import os
import subprocess
import sqlite3
import hashlib

def get_user(conn, user_id):
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return cursor.fetchone()

def run_cmd(user_input):
    os.system("echo " + user_input)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

API_KEY = "sk-ant-api03-9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0b9c8d7e6f"