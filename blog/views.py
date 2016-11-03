# -*- coding: utf-8 -*-
from django.http import JsonResponse
import json
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from blog.models import Post,SomeText
from django.views.generic import ListView, DetailView
from django.core import serializers

# Create your views here.

class PostsListView(ListView):	# представление в виде списка
	model = Post					# модель для представления

class PostDetailView(DetailView):	# детализированное представление модели
	model = Post

def submit_ajax(request):
	text_list = SomeText.objects.all()
	response_data = {}
	if request.method == "POST":
		a = request.POST.get('the_post')
		SomeText(text=a).save()
		response_data['text'] = a
		return JsonResponse(response_data)
	return render(request,'blog/ajax.html',{'text_list':text_list})

def delete_all_objects(request):
	if request.method == "POST":
		SomeText.objects.all().delete()
		return HttpResponse()

def search_posts(request):
	if request.method == "POST":
		search_text = request.POST.get('search_text')
		result = SomeText.objects.filter(text__contains = search_text)
	qs_as_dict = serializers.serialize('python', result)
	results = {}
	results['objects'] = qs_as_dict
	return JsonResponse(results)

def submit(request):
		a=0
		response_data = {}
		if request.method == "POST":
			a = request.POST.get('the_post')
			response_data['text'] = a
			return HttpResponse(a)
