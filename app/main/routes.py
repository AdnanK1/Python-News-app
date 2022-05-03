from flask import render_template
from . import main
from ..request import get_news

@main.route('/')
@main.route('/home')
def home_page():
    news = get_news()
    return render_template('home.html', articles = news)