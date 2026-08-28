import sqlite3
import subprocess
import re
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")          # dane od użytkownika (niezaufane)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # BEZPIECZNE: zapytanie parametryzowane — user_id przekazany jako parametr
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))

    return str(cursor.fetchall())

@app.route("/run")
def run_cmd():
    cmd = request.args.get("cmd", "").strip()  # dane od użytkownika
    # Walidacja: dozwolone tylko bezpieczne znaki hosta/IP
    if not cmd or not re.fullmatch(r"[A-Za-z0-9.-]{1,255}", cmd):
        return "invalid cmd", 400

    app.run(debug=False)                       # debug disabled for safety
    subprocess.run(["ping", "-c", "1", cmd], check=False, capture_output=True, text=True)
    return "done"

if __name__ == "__main__":
    app.run(debug=False)                        # PODATNE: debug=True
