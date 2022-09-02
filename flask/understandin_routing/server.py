from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/dojo')
def Dojo():
    return 'Dojo!'

@app.route('/say/flask')
def flask():
    return 'Hi flask!'

@app.route('/say/<name>')
def hi_John(name):
    return f'Hi {name}!'

@app.route('/repeat/<word>/<int:number>')
def repeat(word, number):
    return word * number

@app.route('/unknown')
def unknown();
    if 


if __name__=="__main__":
    app.run(debug=True)

