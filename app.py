from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>Hello World! my first flask webapp.</h1>'

@app.route("/about")
def about():
    return '<h1>This is about page</h1>'

@app.route("/contact")
def contact():
    return '<h1>This is contact page</h1>'

@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == "POST":
        return "you sent data"
    else:
        return "you are only viewing form"



if __name__ == '__main__':
    app.run(debug=True)

