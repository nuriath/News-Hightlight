from flask import render_template
from app import app
from .request import get_source
from .request import get_articles,get_source 

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
     
    title = 'Home - Welcome to The best News Website Online'

    entertainment_source = get_source('entertainment')
    business_source = get_source('business')
    sport_source = get_source('sports')

    return render_template('index.html', title = title,  entertainment = entertainment_source, business=business_source, sports = sport_source)
    
        # for articles --> 


@app.route('/article/<id>')
def article(id):

    articles= get_articles(id)
      

    return render_template('article.html', articles=articles)






