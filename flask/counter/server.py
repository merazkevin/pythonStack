from flask import Flask, render_template, redirect, request,session
app = Flask(__name__)
app.secret_key='root'  



@app.route('/create_User', methods=['POST'])
def create_user():
    print(request.form)
    session['name']=request.form['name']
    session['email']=request.form['email']
    return redirect('/show_info')

@app.route('/show_info')
def display_userInfo():
    name=session['name']
    email=session['email']
    return render_template( 'display_User.html', name= name, email = email)

#<----- this is for the counter------>
@app.route('/')
def index():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("counter.html")

@app.route('/reset', methods=['POST'])
def reset_visits():
    session.clear()
    return redirect ('/')

@app.route('/x2',  methods=['POST'])
def add2Visits():
    session['count']+=1
    print(request.form)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)