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



    # es.indices.create(
    #     index='test-index',
    #     body={
    #         "settings": {
    #             "index": {
    #                 "analysis": {
    #                     "tokenizer": {
    #                         "nori_user_dict": {
    #                             "type": "nori_tokenizer",
    #                             "decompound_mode": "mixed",
    #                             "user_dictionary": "userdict_ko.txt"
    #                         }
    #                     },
    #                     "analyzer": {
    #                         "my_analyzer": {
    #                             "type": "custom",
    #                             "tokenizer": "nori_user_dict"
    #                         }
    #                     }
    #                 }
    #             }
    #         },
    #         "mappings": {
    #             "navercafe_datas": {
    #                 "properties": {
    #                     "id": {
    #                         "type": "integer"
    #                     },
    #                     "title": {
    #                         "type": "text",
    #                         "analyzer": "my_analyzer"
    #                     },
    #                     "contents": {
    #                         "type": "text",
    #                         "analyzer": "my_analyzer"
    #                     }
    #                 }
    #             }
    #         }
    #     }
    # )
    # body = ""
    # print(b.indexing() for b in models.Navercafe.objects.all().iterator())
    # for b in models.Navercafe.objects.all().iterator():
    #     print(b.indexing())

    # navercafe = models.Navercafe.objects.all()
    # serializer = NavercafeSerializer(navercafe, many=True)
    # for b in serializer:
    #     body = body + json.dumps({"index": {"_index": "test-index", "_type": "navercafe_datas"}}) + '\n'
    #     body = body + json.dumps(b, ensure_ascii=False) + '\n'
    # es.bulk(body)


    bulk(client=es, actions=(b.indexing() for b in models.ProductInfo.objects.all().iterator()))

def search(display):
    s = Search().filter('match', display=display)
    response = s.execute()
    return response