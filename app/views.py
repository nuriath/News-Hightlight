from flask import render_template
from app import app
from .request import get_news,get_news_source
from .request import get_articles
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


# @app.route('/get_news_source/<int:id>')
# def get_news_source(id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     news = get_news_source(id)
#     name = f'{news.name}'

@app.route('/articles/<sources_id>')  
def articles()
  
    author_articles = get_articles('author')
    title_articles = get_articles('title')
    urlToImage_articles = get_articles('urlToImage')
    content_articles = get_articles('content')
   

  return render_template('news.html',title = title, sources_id = author_articles)




