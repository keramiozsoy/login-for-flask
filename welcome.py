from flask import Flask
app = Flask(__filename__)

@app.route("/")
def index():
    return "welcome page!!"

if __filename__ == "__main__":
    app.run(host='0.0.0.0',port=8888)
