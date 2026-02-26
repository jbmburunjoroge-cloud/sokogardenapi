from flask import *


# initialise your flask application
app=Flask(__name__)

# create route
@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to Home Api"})

# create the product route
@app.route("/api/product")
def product():
    return jsonify({"Message":"Welcome to product Api"})

# create the service route
@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to Our Services API"})

# a route for adding two numbers
@app.route("/api/calc",methods=["POST"])
def calc():
    # request the data
    num1=request.form["num1"]
    num2=request.form["num2"]

    sum=int(num1)+int(num2)

    return jsonify({"Answer":sum})

# a route for multiplying two numbers
@app.route("/api/multiply",methods=["POST"])
def multiply():
    # request the data
    num1=request.form["num1"]
    num2=request.form["num2"]


    multiply=int(num1)*int(num2)

    return jsonify({"Answer":multiply})

app.run(debug=True)