from app import app
import urllib.request,json
from .models import source
from .models import article

Source = source.Source
Articles = article.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]
article_base_url = app.config["ARTICLE_API_BASE_URL"]
def get_source(category):
        '''
        Function that gets the json response to our url request
        '''
        get_source_url = base_url.format(category,api_key)

        with urllib.request.urlopen(get_source_url) as url:
            get_source_data = url.read()
            get_source_response = json.loads(get_source_data)

            new_sources = None

            if get_source_response['sources']:
                new_sources_list = get_source_response['sources']
                new_sources = process_sources(new_sources_list) 
        return new_sources
    
def process_sources(new_list):
        '''
        Function  that processes the source result and transform them to a list of Objects

        Args:
            source_list: A list of dictionaries that contain source details

        Returns :
            source_sources: A list of source objects
        '''
        sources_sources = []
        for sources_item in new_list:
            id = sources_item.get('id')
            name = sources_item.get('name')
            description = sources_item.get('description')
            url = sources_item.get('url')
            category = sources_item.get('category')
            language = sources_item.get('language')
            country = sources_item.get('country')

            if name:
                source_object = Source(id,name,description,url,category,language,country)
                sources_sources.append(source_object)


        return sources_sources
#-----------------------------------------------------

def get_articles(id):
        '''
        Function that gets the json response to our url request
        '''
        get_articles_url = article_base_url.format(id,api_key)

        with urllib.request.urlopen(get_articles_url) as url:
            get_articles_data = url.read()
            get_articles_response = json.loads(get_articles_data)

            article_articles = None

            if get_articles_response['articles']:
                article_articles_list = get_articles_response['articles']
                article_articles = process_articles(article_articles_list) 
        return article_articles
    
def process_articles(article_list):
        '''
        Function  that processes the article result and transform them to a list of Objects

        Args:
            article_list: A list of dictionaries that contain article details

        Returns :
            article_articles: A list of article objects
        '''
        articles_articles = []
        for articles_item in article_list:
            author  =articles_item.get('author ')
           
            title =articles_item.get('title')
            description=articles_item.get('description')
            urlToImage =articles_item.get('urlToImage')
            content =articles_item.get('content')
            
            if title:
                article_object = Articles(author,title,description,urlToImage,content)
                articles_articles.append(article_object)


        return articles_articles

# def get_source(id):
#     get_source_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_source_details_url) as url:
#         source_details_data = url.read()
#         source_details_response = json.loads(source_details_data)

#         source_object = None
#         if source_details_response:
#             id = source_details_response.get('id')
#             name = source_details_response.get('name')
#             description = source_details_response.get('description')
#             url = source_details_response.get('url')
#             category = source_details_response.get('category')
#             language = source_details_response.get('language')
#             country = source_details_response.get('country')

#             source_object = Source(id,name,description,url,category,language,country)

#     return source_object





















