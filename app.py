from flask import Flask, render_template , url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('WelcomePage.html')

@app.route("/apply")
def apply():
    return render_template('ApplyPage.html')
    
if __name__ == "__main__":
    app.run(debug=True)