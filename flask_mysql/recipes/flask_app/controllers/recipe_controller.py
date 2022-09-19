from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models import recipe_model



@app.route('/')
def index():
    return render_template('register_and_login.html')