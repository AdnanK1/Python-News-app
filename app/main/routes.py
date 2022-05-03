from flask import render_template
from . import main

@main.route('/')
@main.route('/home')
def home_page():
    return render_template('home.html')