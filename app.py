from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else :
        return "There is something wrong with it"


if __name__ == '__main__':
    app.run(debug=True)

