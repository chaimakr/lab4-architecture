from flask import Flask, render_template, jsonify, request
import os 
from flask_sqlalchemy import SQLAlchemy 


def create_the_database(db):
    db.create_all()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'A secret'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db' # for using the sqlite database

db = SQLAlchemy(app)

class Client(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    salary = db.Column(db.Integer)
    financialSituation = db.Column(db.String(50))
    age = db.Column(db.Integer)
    amount = db.Column(db.String(50))
    otherloans= db.Column(db.String(50))

@app.route('/risk/assess',methods=["POST"])
def asses_risk():
    firstname=request.json['firstname']
    lastname=request.json['lastname']
    salary=request.json['salary']
    financialSituation=request.json['financialSituation']
    age=request.json['age']
    loanAmount=request.json['loanAmount']
    loanDuration=request.json['loanDuration']
    loanPurpose=request.json['loanPurpose']
    initialScore=request.json['initialScore']
    person=Client.query.filter_by(firstname=firstname).first()
    response = {}
    print(person)
    if person :
        if person.otherloans =="no":
            if person.financialSituation =="bad":
                response["data"]="35"
            elif int(person.amount) < 5000:
                response["data"]="45"
            else : 
                response["data"]="70"
        else :
            response["score"]="20"
    else:
        response["score"]="No user by these credentials!"
    
    return response


db_is_new = not os.path.exists('account.db')
if db_is_new:
    create_the_database(db)



if __name__ == "__main__":
  app.run()
