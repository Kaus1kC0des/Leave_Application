from flask import Flask, render_template, request

app = Flask(__name__,template_folder='./templates',static_folder="./static")


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
