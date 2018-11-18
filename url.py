from flask import Flask
from flask import render_template
from flask import json
from flask import Response

from digger.databases import core
from digger.databases import cedet
from digger.databases import loja_integrada

app = Flask(__name__,
static_folder="./dist/static",
template_folder="./dist")

@app.route('/') 
def hello_world(): 
    return render_template("index.html")

@app.route('/api/<bookStore>/book/<bookName>', methods=['GET']) 
def getStoreBooks(bookStore,bookName):
    getBook = core.getBookStore(bookStore) 
    js = json.dumps(getBook(bookName))
    resp = Response(js, status=200, mimetype='application/json')
    return resp