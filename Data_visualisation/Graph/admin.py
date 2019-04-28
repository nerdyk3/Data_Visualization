from django.contrib import admin
from .models import Graph_Key,Graph_name,suggestion,GraphType


class Graph_nameAdmin(admin.ModelAdmin):
	 list_filter =('key_name',)


admin.site.register(Graph_Key)
admin.site.register(Graph_name,Graph_nameAdmin)
admin.site.register(suggestion)
admin.site.register(GraphType)
