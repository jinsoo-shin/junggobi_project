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
        if search_word:
            es = Elasticsearch()
            docs = es.search(index='productinfo-index',
                             body={
                                 "query": {
                                     "multi_match": {
                                         "query": search_word,
                                         "fields": ["title", "contents", "region"]
                                     }
                                 }
                             })

            data_list = docs['hits']
            print(data_list)
            return Response(data_list)

    if request.method == 'POST':
        search = request.data.get('search', None)
        if search:
            es = Elasticsearch()
            es.indices.delete(index='productinfo-index', ignore=[400, 404])
        bulk_indexing()
        return Response(data=search,status=status.HTTP_200_OK)

