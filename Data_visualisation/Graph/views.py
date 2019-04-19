from django.shortcuts import render, redirect,HttpResponse
from .models import csvimport, graph_axis,GraphType
from .forms import DataForm , PlotForm
import pandas as pd
import pdb
from django.template import Context, Template
import seaborn as sys
import matplotlib.pyplot as mlt
# import cufflinks as cf

# Create your views here.

def index(request):
	if request.method == "POST":
		x = DataForm(request.POST, request.FILES)
		if x.is_valid():
			data = x.save(commit=False)
			#data.save()
			FileRead = data.file
			ReadCSV = pd.read_csv(FileRead)
			KeyCSV = ReadCSV.keys()
			ReadFile(data,ReadCSV)
			return render(request,'Graph/success.html',{'y':ReadCSV,'r':GraphType.objects.all()})

	else:
		x = DataForm()
		return render(request, 'Graph/index.html',{'x':x})

def app(request):
    return render(request,'Graph/app.html')

def ReadFile(data,File):
	# if get_object_or_404(csvimport, pk=pk):
	global f,z
	z=data
	f = File
	return f

def graph(request):
	#pdb.set_trace()
	if request.method == "POST":
		MaP=PlotForm(request.POST)
		if MaP.is_valid():
			data = MaP.save(commit=False)
			Graphtype(data)
			return redirect('../')


	else:
		MaP = PlotForm()
		return render(request,'placio_month/success.html',{'MaP':MaP})

def Graphtype(typegarph):
	if typegarph.graphName == "ColumnBarGraphs":
		mlt.subplots(figsize=(10,7))
		sys.countplot(x=typegarph.x_axis,hue=typegarph.hue, data=f).set_title(z.description)
		return mlt.show()
	if typegarph.graphName == "FacetGrid":
		mlt.subplots(figsize=(10,7))
		sys.relplot(x=typegarph.x_axis, y=typegarph.hue, hue=typegarph.hue, data=f)
		return mlt.show()
	# if typegarph.graphName == "LinePlot":
	# 	mlt.subplots(figsize=(10,7))
	# 	sys.lineplot(x=typegarph.x_axis, y=typegarph.hue, hue=typegarph.hue,data=f)
	# 	return mlt.show()
	# if typegarph.graphName == "ColumnBarGraphs":
	# 	mlt.subplots(figsize=(10,7))
	# 	sys.barplot(x=typegarph.x_axis,y=typegarph.hue,hue=typegarph.hue, data=f).set_title(z.description)
	# 	return mlt.show()
def aboutme(request):
	return render(request,'placio_month/about-me.html')