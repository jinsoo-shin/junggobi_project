from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Keyword, Text, Integer, Date,Search,tokenizer,analyzer,analysis,Boolean

from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models
import json

connections.create_connection(hosts=['localhost'])
my_analyzer = analyzer(
    'my_analyzer',
    tokenizer=tokenizer('nori_tokenizer')
)
# ngram_analyzer = analyzer(
#     'ngram_analyzer',
#     tokenizer=tokenizer('edge_ngram',min_gram=1,max_gram=20),
#     filter=['lowercase']
# )

class ProductInfoIndex(Document):

    id = Integer()
    category = Text()
    manufacturer = Text(analyzer=my_analyzer)
    model_name = Text(analyzer=my_analyzer)
    generation = Text()
    display = Text()
    cellular = Text()
    storage = Text(analyzer=my_analyzer)
    price = Integer()
    region = Text(analyzer=my_analyzer)
    date = Date()
    link = Text()
    img_src = Text()
    is_sell = Integer()
    title = Text(analyzer=my_analyzer)
    contents = Text(analyzer=my_analyzer)
    # class Meta:
    #     index = 'navercafe-index'
    class Index:
        name = 'productinfo-index'



def bulk_indexing():
    ProductInfoIndex.init()
    es = Elasticsearch()

    bulk(client=es, actions=(b.indexing() for b in models.ProductInfo.objects.all().iterator()))

def search(display):
    s = Search().filter('match', display=display)
    response = s.execute()
    return response