import os

from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
#es = Elasticsearch('127.0.0.1', port=9200)
es_host = os.environ['DOCKER_MACHINE_IP']
es = Elasticsearch([es_host])


@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    search_term = request.form["input"]
    res = es.search(
        index="method", 
        size=20, 
        body={
            "query": {
                "multi_match" : {
                    "query": search_term, 
                    "fields": [
                        "state"
                    ] 
                }
            }
        }
    )
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
