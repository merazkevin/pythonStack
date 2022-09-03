from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def header():
    return render_template('index.html')

@app.route('/play/<int:number>')
def playground(number):
    return render_template('play.html', number=number)
    





if __name__=="__main__":
    app.run(debug=True)