from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask + MySQL Docker Project 🚀"

@app.route('/db')
def db():
    conn = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",
        database="testdb"
    )
    return "Connected to MySQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
