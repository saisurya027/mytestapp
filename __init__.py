from flask import Flask,request

app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def hello():
    return request.form['Poll']
    return "Hello World!"

if __name__ == "__main__":
    app.run()