from flask import Flask, jsonify
import requests
from psycopg2 import connect

app = Flask(__name__)

connection_string = "postgres://postgres:postgres@localhost:5432/jordan"
client = connect(connection_string)

@app.route('/')
def hello_world():
   return "Hello World"

@app.route('/math-test')
def math_test():
    limit = 10 * 10 ** 8
    numerator = 0
    denominator = 1
    result = 0
    for _ in range(limit):
        result += numerator / denominator
        numerator += 1
        denominator += 1
    return str(result)

@app.route('/get-from-db')
def get_from_db():
    with client.cursor() as cursor:
        cursor.execute("SELECT * FROM data")
        res = cursor.fetchall()
        return jsonify(data=res)

@app.route('/write-to-db')
def write_to_db():
    with client.cursor() as cursor:
        cursor.execute("INSERT INTO data VALUES (333)")
        return "OK"

@app.route('/get-from-api')
def get_from_api():
    r = requests.get('https://httpbin.org/get')
    return r.json()


if __name__ == '__main__':
   app.run()