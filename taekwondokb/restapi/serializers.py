from rest_framework.serializers import ModelSerializer
from encyclopedia.models import Volume, Page
from regulations.models import Belt, Regulation

class VolumeSerializer(ModelSerializer):
    class Meta:
        model = Volume
        fields = "__all__"

class PageLinkSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = ['page', 'title']

class PageSerializer(ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class BeltSerializer(ModelSerializer):
    class Meta:
        model = Belt
        fields = "__all__"

class RegulationSerializer(ModelSerializer):
    class Meta:
        model = Regulation
        fields = "__all__"