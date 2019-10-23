import datetime
from haystack import indexes
from api.models import Navercafe


class NavercafeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,template_name='search/navercafe_text.txt')
    title = indexes.CharField(model_attr='title',null=True)
    contents = indexes.CharField(model_attr='contents',null=True)

    id = indexes.IntegerField(model_attr='id')
    category = indexes.CharField(model_attr='category',null=True)
    manufacturer = indexes.CharField(model_attr='manufacturer',null=True)
    model_name = indexes.CharField(model_attr='model_name',null=True)
    generation = indexes.CharField(model_attr='generation',null=True)
    display = indexes.CharField(model_attr='display',null=True)
    cellular = indexes.CharField(model_attr='cellular',null=True)
    storage = indexes.CharField(model_attr='storage',null=True)
    price = indexes.IntegerField(model_attr='price',null=True)
    region = indexes.CharField(model_attr='region',null=True)
    date = indexes.DateField(model_attr='date',null=True)
    link = indexes.CharField(model_attr='link',null=True)
    img_src = indexes.CharField(model_attr='img_src',null=True)
    is_sell = indexes.BooleanField(model_attr='is_sell',null=True)

    def get_model(self):
        return Navercafe

    def index_queryset(self, using=None): ##인덱싱할 객체들 거르기
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()