from elasticsearch import Elasticsearch
from django_elasticsearch_dsl import Document,fields,Index
from api.models import Navercafe

class NavercafeDocument(Document):
    id = fields.IntegerField()
    category = fields.TextField()
    manufacturer = fields.TextField()
    model_name = fields.TextField()
    generation = fields.TextField()
    display = fields.TextField()
    cellular = fields.TextField()
    storage = fields.TextField()
    price = fields.IntegerField()
    region = fields.TextField()
    date = fields.DateField()
    link = fields.TextField()
    img_src = fields.TextField()
    is_sell = fields.IntegerField()
    title = fields.TextField()
    contents = fields.TextField()

    class Index:
        # Name of the Elasticsearch index
        name = 'navercafe_index'

    class Django:
        model = Navercafe
        fields = [
            'id',
            'category',
            'manufacturer',
            'model_name',
            'generation',
            'display',
            'cellular',
            'storage',
            'price',
            'region',
            'date',
            'link',
            'img_src',
            'is_sell',
            'title',
            'type',
            'contents',
        ]

