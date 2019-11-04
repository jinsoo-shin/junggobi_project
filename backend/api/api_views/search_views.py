from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TabletSerializer, ProductSerializer, Product_Info_Serializer
from api.models import Tablet, Product, ProductInfo
import datetime
from django.db import connection, connections
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from api.search import bulk_indexing


@api_view(['GET', 'POST'])
def search(request):
    if request.method == 'GET':
        search_word = request.query_params.get('search_word')
        if search_word is not "":
            es = Elasticsearch()
            docs = es.search(index='productinfo-index',
                             body={
                                 "size": 200, # size는 한 번에 나타날 게시글의 수
                                 "from": 0, # 페이징을 할 때 쪽수는 from
                                 "query": {
                                     "bool": {
                                         "should": [
                                             {"match": {"title": search_word}},
                                             {"match": {"contents": search_word}},
                                             {"match": {"region": search_word}},
                                             {"match": {"model_name": search_word}}
                                         ]
                                     }
                                 },
                                 "highlight": {
                                     "pre_tags": ["<mark><strong>"],
                                     "post_tags": ["</strong></mark>"],
                                     "fields": {
                                         "title": {},
                                         "contents":{}
                                     },
                                 },
                                 "aggs": {#aggregations
                                     "avg_price": {
                                         "avg": {
                                             "field": "price"
                                         }
                                     },
                                     "max_price": {
                                         "max": {
                                             "field": "price"
                                         }
                                     },
                                     "min_price": {
                                         "min": {
                                             "field": "price"
                                         }
                                     },
                                     "group_by_date": {
                                         "terms": {
                                             "field": "date",
                                             "format": "yyyy-MM-dd",
                                             "order": {"_key": "asc"},
                                             "size": 7
                                         },
                                         "aggs": {
                                             "date_avg": {
                                                 "avg": {
                                                     "field": "price"
                                                 },
                                             },
                                             "date_max": {
                                                 "max": {
                                                     "field": "price"
                                                 }
                                             },
                                             "date_min": {
                                                 "min": {
                                                     "field": "price"
                                                 }
                                             },
                                         },
                                     },

                                 }
                             })

            return Response(docs)
        else:
            es = Elasticsearch()
            docs = es.search(index='productinfo-index',
                             body={
                                 "size": 2000, # size는 한 번에 나타날 게시글의 수
                                 "from": 0, # 페이징을 할 때 쪽수는 from
                                 "query": {
                                    "match_all": {}
                                 },
                                 "aggs": {#aggregations
                                     "avg_price": {
                                         "avg": {
                                             "field": "price"
                                         }
                                     },
                                     "max_price": {
                                         "max": {
                                             "field": "price"
                                         }
                                     },
                                     "min_price": {
                                         "min": {
                                             "field": "price"
                                         }
                                     },
                                     "group_by_date": {
                                         "terms": {
                                             "field": "date",
                                             "format": "yyyy-MM-dd",
                                             "order": {"_key": "asc"},
                                             "size": 7
                                         },
                                         "aggs": {
                                             "date_avg": {
                                                 "avg": {
                                                     "field": "price"
                                                 },
                                             },
                                             "date_max": {
                                                 "max": {
                                                     "field": "price"
                                                 }
                                             },
                                             "date_min": {
                                                 "min": {
                                                     "field": "price"
                                                 }
                                             },
                                         },
                                     },

                                 }
                             })

            return Response(docs)


    if request.method == 'POST':
        search = request.data.get('search', None)
        if search:
            es = Elasticsearch()
            es.indices.delete(index='productinfo-index', ignore=[400, 404])
            print("index delete")
        bulk_indexing()
        return Response(data=search,status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def auto(request):
    if request.method == 'GET':
        search_word = request.query_params.get('search_word')
        if search_word:
            word = search_word.replace(" ","").split()
            es = Elasticsearch()
            docs = es.search(index='productinfo-index',
                             body={
                                 "size":10,
                                 "_source": ["model_name"],
                                    "query": {
                                     "wildcard": {
                                         "model_name": {
                                             "value": "*"+search_word+"*"
                                         }
                                     },
                                 },
                           
                             })

            request_result = docs['hits']['hits']
            # return Response(request_result)
            auto_keyword=[] 
            for data in request_result:
                auto_keyword.append(data["_source"]['model_name'])
            auto_keyword = list(set(auto_keyword))
            auto_keyword.sort(key = lambda s: len(s))
            return Response(auto_keyword)
