from flask import Flask,render_template,request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "no secrets on github  "




@app.route('/')          # The "@" decorator associates this route with the function immediately following
def render_form():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/process_form', methods=['POST'])
def process_form():
    print(request.form)
    session['dog_name'] = request.form['dog_name']
    session['dog_breed'] = request.form['dog_breed']
    return redirect('/show_info')

@app.route('/show_info')
def show_info():
    name = session['dog_name']
    breed = session['dog_breed']
    return render_template("display.html", name=name, breed=breed)

@app.route('/clear_session')
def clear_session():
    session.clear() #clears session
    # del session['dog_breed'] #would revome the dog_breed key
    # dog_name=session.pop(dog_name)
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)  