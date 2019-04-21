from django import forms
from .models import csvimport,graph_axis
from .models import Graph_name

class DataForm(forms.ModelForm):

	class Meta:
		model = csvimport
		fields = ('description', 'file', )

class PlotForm(forms.ModelForm):

	class Meta:
		model = graph_axis
		fields = ('graphName','x_axis', 'hue',)

class Graph_nameForm(forms.ModelForm):
	class Meta:
		model = Graph_name
		fields = ('key_name','graph_name',)

