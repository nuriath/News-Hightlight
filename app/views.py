from flask import render_template
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     
    title = 'Home - Welcome to The best News Website Online'
    entertainment_news = get_news('entertainment')
    business_news = get_news('business')
    sport_news = get_news('sport')

    print(entertainment_news, business_news, sport_news)
    
    return render_template('index.html', title = title,  entertainment = entertainment_news, business =business_news, sport = sport_news)


