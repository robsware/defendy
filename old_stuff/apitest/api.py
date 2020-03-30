import flask
import os 
import sys
from flask import request

app = flask.Flask(__name__)



@app.route('/rename', methods=['GET'])

def my_route():
  page = request.args.get('page', default = 1, type = int)
  filterStuff = request.args.get('filter', default = '*', type = str)
  os.mkdir("bbbbbb" + str(page) + str(filterStuff))
  return("Ok")

app.run()