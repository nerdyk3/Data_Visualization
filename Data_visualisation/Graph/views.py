from django.shortcuts import render, redirect,HttpResponse
from django.http import JsonResponse
from .models import Graph_Key,Graph_name, csvimport, graph_axis,GraphType
from .forms import Graph_nameForm,DataForm,PlotForm,suggestionForm
import pandas as pd
import pdb
from django.template import Context, Template
import seaborn as sys
import matplotlib.pyplot as mlt
from .serializers import Graph_KeySerializer,Graph_nameSerializer
import networkx as nx
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
		request.session['keyname'] = keyname
		request.session['graphname'] = graphname
		graph_detail = Graph_name.objects.filter(graph_name = graphname) 
		return render(request,'Graph/file.html',{'graph_detail':graph_detail,'keyname':keyname,'graphname':graphname})

def networkx(request):
	if request.method == "POST":
		if request.session['graphname'] == 'dodecahedral_graph':
			data_network = request.POST.get('dodecahedral_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'lollipop_graph':
			data_network = request.POST.get('lollipop_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'grid_2d_graph':
			data_network = request.POST.get('grid_2d_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'house_graph':
			data_network = request.POST.get('house_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'star_graph':
			data_network = request.POST.get('star_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'cycle_graph':
			data_network = request.POST.get('cycle_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'path_graph':
			data_network = request.POST.get('path_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'petersen_graph':
			data_network = request.POST.get('petersen_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		if request.session['graphname'] == 'cubical_graph':
			data_network = request.POST.get('cubical_graph')
			G = nx.dodecahedral_graph()
			shells =  data_network
			nx.draw(G)
		return mlt.show()

def ReadDoc(request):
	if request.method == "POST":
		if request.session['keyname'] == 'NetworkX':
			pass
		else:
			x = DataForm(request.POST, request.FILES)
			if x.is_valid():
				data = x.save(commit=False)
				#data.save()
				FileRead = data.file
				ReadCSV = pd.read_csv(FileRead)
				KeyCSV = ReadCSV.keys()
				ReadFile(data,ReadCSV)
				keyname = request.session['keyname']
				graphname = request.session['graphname']
				return render(request,'Graph/success.html',{'y':ReadCSV,'keyname':keyname,'graphname':graphname})

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




def suggestion(request):
	if request.method == "POST":
		x = suggestionForm(request.POST)
		if x.is_valid():
			data = x.save(commit=False)
			data.save()
			return HttpResponse('Thank You for make suggestion with us, we will contact you shortly.')

	else:	
		x = suggestionForm()
		return render(request,'Graph/suggestion.html')