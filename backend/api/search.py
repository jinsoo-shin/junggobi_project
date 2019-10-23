from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Keyword, Text, Integer, Date,Search,tokenizer,analyzer

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
connections.create_connection(hosts=['localhost'])

class NavercafeIndex(Document):
    id = Integer()
    category = Text()
    manufacturer = Text()
    model_name = Text()
    generation = Text()
    display = Text()
    cellular = Text()
    storage = Text()
    price = Integer()
    region = Text()
    date = Date()
    link = Text()
    img_src = Text()
    is_sell = Integer()
    title = Text()
    contents = Text()
    # class Meta:
    #     index = 'navercafe-index'
    class Index:
        name = 'navercafe-index'

def bulk_indexing():
    NavercafeIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Navercafe.objects.all().iterator()))

def search(display):
    s = Search().filter('match', display=display)
    response = s.execute()
    return response