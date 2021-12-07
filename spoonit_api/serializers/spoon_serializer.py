from rest_framework import serializers
from spoonit_api.models import Spoon

class SpoonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spoon
        fields = ('id', 'number_of_spoons')
        depth = 1



