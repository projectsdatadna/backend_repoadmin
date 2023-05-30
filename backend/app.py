import mysql.connector
from flask import Flask,jsonify
from datetime import datetime
from flask_cors import CORS

app=Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
now = datetime.now()

mydb = mysql.connector.connect(
    user='root', password='', host='localhost', database='account')


if mydb:
    print ("Connected Successfully")
else:
    print ("Connection Not Established")

mycursor = mydb.cursor()
def fetch_db(sqlquery):
    mycursor.execute(sqlquery)
    return mycursor.fetchall()
   
@app.route('/users', methods=['GET'])
def my_values():
    return jsonify(fetch_db(sqlquery="SELECT * FROM `values`"))

@app.route('/count', methods=['GET'])
def my_count():
    return jsonify(fetch_db(sqlquery="SELECT count(*) FROM `values`"))
    

@app.route('/orders', methods=['GET'])
def my_order():
    return jsonify(fetch_db(sqlquery="SELECT * FROM `orders`"))

@app.route('/earnings', methods=['GET'])
def my_earnings():
    return jsonify(fetch_db(sqlquery="SELECT * FROM `orders` WHERE `status`='Completed'"))

@app.route('/balance', methods=['GET'])
def my_balance():
    return jsonify(fetch_db(sqlquery="SELECT * FROM `orders` WHERE `status`='Pending'"))

if __name__ == "__main__":
    app.run(debug=True)
    