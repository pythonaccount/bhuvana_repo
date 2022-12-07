from rest_framework.serializers import ModelSerializer

from .models import Data


class DataSerializers(ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'
