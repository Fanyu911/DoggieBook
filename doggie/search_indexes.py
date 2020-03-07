from doggie.models import Dog
from haystack import indexes


class GoodsInfoIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)
    dog_name = indexes.CharField(model_attr='dog_name')
    short_description = indexes.CharField(model_attr='short_description')
    long_description = indexes.CharField(model_attr='long_description')
    life_span = indexes.CharField(model_attr='life_span')
    price = indexes.CharField(model_attr='price')
    rendered = indexes.CharField(use_template=True, indexed=False)

    def get_model(self):
        return Dog


    def index_queryset(self, using=None):
        return self.get_model().objects.all()
