from flask import Flask, render_template, request, redirect
from user import User

app = Flask(__name__)
@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users=all_users)

@app.route('/newUser')
def newUser():
    return render_template("newUser.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    # print("*******deleteRoute*******",request.form)
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        'id':id
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.delete(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)