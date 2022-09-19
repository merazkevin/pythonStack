from flask_app import app, bcrypt
from flask import render_template, request, redirect, session,flash
from flask_app.models import template_model



@app.route('/')
def index():
    return render_template('index.html')