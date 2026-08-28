import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    user_id = request.args.get("id")          # dane od użytkownika (niezaufane)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # PODATNE: SQL injection — user_id wklejony wprost do zapytania
    query = "SELECT * FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)

    return str(cursor.fetchall())

@app.route("/run")
def run_cmd():
    import os
    cmd = request.args.get("cmd")             # dane od użytkownika
    # PODATNE: Command injection — dane usera trafiają do os.system
    os.system("ping " + cmd)
    return "done"

if __name__ == "__main__":
    app.run(debug=True)                        # PODATNE: debug=True
