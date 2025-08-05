# src/app.py
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cur.execute(query)
    result = cur.fetchone()
    return "Login Successful" if result else "Login Failed"

if __name__ == "__main__":
    app.run()
