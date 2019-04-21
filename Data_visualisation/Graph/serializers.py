from django.db.models import Count
from rest_framework import serializers
from .models import Graph_Key,Graph_name

class Graph_KeySerializer(serializers.ModelSerializer):
	class Meta:
		model =Graph_Key
		fields = '__all__'


class Graph_nameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Graph_name
		fields = '__all__'