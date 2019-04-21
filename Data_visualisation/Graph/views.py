from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from .models import Graph_Key,Graph_name, csvimport, graph_axis,GraphType
from .forms import Graph_nameForm,DataForm,PlotForm
import pandas as pd
import pdb
from django.template import Context, Template
import seaborn as sys
import matplotlib.pyplot as mlt
from .serializers import Graph_KeySerializer,Graph_nameSerializer
# import cufflinks as cf

# Create your views here.

def index(request):
	return render(request,'Graph/index.html')

def file(request):
	if request.method == "POST":
		x = DataForm(request.POST, request.FILES)
		if x.is_valid():
			data = x.save(commit=False)
			FileRead = data.file
			ReadCSV = pd.read_csv(FileRead)
			KeyCSV = ReadCSV.keys()
			ReadFile(data,ReadCSV)
			graph_key = Graph_Key.objects.all()
			key_names = Graph_name.objects.all()
			return render(request,'Graph/app.html',{'y':ReadCSV,'key':graph_key,'key_names':key_names})

	else:
		x = DataForm()
		return render(request, 'Graph/file.html',{'x':x})

def app(request):
	if request.method == "POST":
		form = Graph_nameForm(request.POST)
		print(request.POST.get('graph_name'))
		key_name = request.POST.get('key_name')
		graph_name = Graph_name.objects.filter(key_name__Key_name = key_name)
		return render(request,'Graph/app.html',{'key_name':key_name,'graph_name':graph_name})

	else:
		graph_key = Graph_Key.objects.all()
		return render(request,'Graph/app.html',{'key':graph_key})

def app_page(request):
	if request.method == "POST":
		form = Graph_nameForm(request.POST)
		keyname = request.POST.get('key_name')
		graphname = request.POST.get('graph_name')
		graph_detail = Graph_name.objects.filter(graph_name = graphname) 
		return render(request,'Graph/file.html',{'graph_detail':graph_detail,'keyname':keyname,'graphname':graphname})

def ReadDoc(request):
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
		return render(request, 'Graph/file.html',{'x':x})

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


# 	else:
# 		MaP = PlotForm()
# 		return render(request,'placio_month/success.html',{'MaP':MaP})

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