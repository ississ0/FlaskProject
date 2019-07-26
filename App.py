from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/hello/<name>')
def index(name):
    return "Hello " + name

@app.route('/profile')
def profile():
    address = request.args.get('address')
    return render_template('introduce.html',
                           address = address)

if __name__ == '__main__':
    app.run()