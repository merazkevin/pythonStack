from flask import Flask, render_template,session, redirect,request
app = Flask(__name__)    
app.secret_key='root'  



@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/process', methods=['POST'])
def processForm():
    session['submitButton']=request.form['submitButton']
    return redirect('/result')

@app.route('/result')
def resultPage():
    return render_template("result.html")
    
    
@app.route('/home')
def returnHome():
    session['home']=request.form['home']
    redirect('/')

# @app.route('/homeButton')
# def homeButton():
#     render_template('index.html')


if __name__=="__main__": 
    app.run(debug=True)