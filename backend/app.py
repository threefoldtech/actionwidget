
import sqlite3
from flask import Flask
app = Flask(__name__)


conn = sqlite3.connect('calltoaction.db')

@app.route('/')
def index():
   return "yo hello"

if __name__ == '__main__':
   app.run(debug = True)