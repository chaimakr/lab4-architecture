from flask import Flask, request
from loan_application import LoanApplication

from person_applier import PersonApplier
from calculate_score import calculate_score


app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Welcome to The Commercial Service</h1>'

@app.route('/postform', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        print(json['firstname'])
        personApplier=PersonApplier(json['userid'],json['firstname'],json['lastname'],json['salary'],json['finantialSituation'],json['age'])
        loanApplication=LoanApplication(json['loanid'],personApplier,json['loanAmount'],json['loanDuration'],json['loanPurpose'])
        print(calculate_score(personApplier.salary,personApplier.finantialSituation,personApplier.age,loanApplication.loanAmount,loanApplication.loanDuration,loanApplication.loanPurpose))
        json['score']=calculate_score(personApplier.salary,personApplier.finantialSituation,personApplier.age,loanApplication.loanAmount,loanApplication.loanDuration,loanApplication.loanPurpose)
        return json
    else:
        return 'Content-Type not supported!'


if __name__ == '__main__':
  app.run()