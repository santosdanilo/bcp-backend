from flask import Flask
from flask import render_template
from flask import json
from flask import Response

from digger.central import getBooksFrom

app = Flask(__name__,
static_folder="./dist/static",
template_folder="./dist")

@app.route('/') 
def index(): 
    return render_template("index.html")

@app.route('/api/<bookStore>/book/<bookName>', methods=['GET']) 
def getStoreBooks(bookStore,bookName):
    books = getBooksFrom(bookStore, bookName) 
    js = json.dumps(books)
    resp = Response(js, status=200, mimetype='application/json')
    return resp