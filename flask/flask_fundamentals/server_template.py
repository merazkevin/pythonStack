from flask import Flask, render_template, redirect, request,session 
app = Flask(__name__)    
app.secret_key='root'  



@app.route('/')          
    


if __name__=="__main__": 
    app.run(debug=True)