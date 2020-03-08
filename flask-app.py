import flask
from flask import request, jsonify
import sqlite3
from newsapi import NewsApiClient
import requests
from google_language import GoogleLanguage
from read_json import body


# Init
newsapi = NewsApiClient(api_key='1f7bbd54c6ef4567a64a3424490e831d')

list_of_entities = (GoogleLanguage().get_entities(body))
string_of_entities = ', '.join(list_of_entities)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d


# @app.route('/', methods=['GET'])
# def home():
#     return '''<h1>Distant Reading Archive</h1>
# <p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/', methods=['GET'])
def api_all():
    return jsonify(newsapi.get_everything(q=string_of_entities))



# @app.errorhandler(404)
# def page_not_found(e):
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404


# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_filter():
#     query_parameters = request.args

#     id = query_parameters.get('id')
#     published = query_parameters.get('published')
#     author = query_parameters.get('author')

#     query = "SELECT * FROM books WHERE"
#     to_filter = []

#     if id:
#         query += ' id=? AND'
#         to_filter.append(id)
#     if published:
#         query += ' published=? AND'
#         to_filter.append(published)
#     if author:
#         query += ' author=? AND'
#         to_filter.append(author)
#     if not (id or published or author):
#         return page_not_found(404)

#     query = query[:-4] + ';'

#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()

#     results = cur.execute(query, to_filter).fetchall()

#     return jsonify(results)

app.run()