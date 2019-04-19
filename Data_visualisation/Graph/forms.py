from django import forms
from .models import csvimport,graph_axis


class DataForm(forms.ModelForm):

	class Meta:
		model = csvimport
		fields = ('description', 'file', )

class PlotForm(forms.ModelForm):

	class Meta:
		model = graph_axis
		fields = ('graphName','x_axis', 'hue',)
