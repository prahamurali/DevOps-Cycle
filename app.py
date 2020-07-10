from flask import Flask, render_template, redirect, url_for
import psycopg2

conn = psycopg2.connect(
    host="localhost", database="devopscycle", user="postgres", password="pgpass")
cur = conn.cursor()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/table')
def table():
    cur.execute("Select * from testtable")
    elts = cur.fetchall()
    print(elts)
    return render_template("table.html", res=elts)


if __name__ == "__main__":
    app.run(debug=True)
