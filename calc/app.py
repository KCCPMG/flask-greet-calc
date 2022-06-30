# Put your app in here.
from flask import Flask, request
from operations import add, mult, div, sub

app = Flask(__name__)


@app.route("/add")
def get_add():
  a = int(request.args["a"])
  b = int(request.args["b"])
  return str(add(a, b))

@app.route("/sub")
def get_sub():
  a = int(request.args["a"])
  b = int(request.args["b"])
  return str(sub(a, b))

@app.route("/mult")
def get_mult():
  a = int(request.args["a"])
  b = int(request.args["b"])
  return str(mult(a, b))

@app.route("/div")
def get_div():
  a = int(request.args["a"])
  b = int(request.args["b"])
  return str(div(a, b))

@app.route("/math/<operation>")
def get_math(operation):
  a = int(request.args["a"])
  b = int(request.args["b"])


  operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
  }

  return str(operations[operation](a, b))

  # if operation == "add":
  #   return str(add(a, b))
  # elif operation == "sub":
  #   return str(sub(a, b))
  # elif operation == "mult":
  #   return str(mult(a, b))
  # elif operation == "div":
  #   return str(div(a, b))
