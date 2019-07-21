from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is my homepage!'

@app.route('/ej')
def index2():
    return render_template('introduce.html')

if __name__ == '__main__':
    app.run()