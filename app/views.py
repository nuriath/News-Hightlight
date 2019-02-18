from flask import render_template
from app import app
from .request import get_news
from .requests import get_news,get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     
    title = 'Home - Welcome to The best News Website Online'
    entertainment_news = get_news('entertainment')
    business_news = get_news('business')
    sport_news = get_news('sports')
    
    return render_template('index.html', title = title,  entertainment = entertainment_news, business=business_news, sports = sport_news)


@app.route('/news/<int:id>')
def news(id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = get_news(id)
    name = f'{news.name}'

    return render_template('news.html',title = title, news = news)