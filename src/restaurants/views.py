from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
	num = random.randint(0,1000000)
	return render(request,"home.html" , {"rand" : num , "test" : " this values will dislplya at apge"})
	#return HttpResponse(html_)

def content(request):
	num = random.randint(0,1000000)
	return render(request,"content.html" , {"rand" : num , "test" : " this values will dislplya at apge"})
	#return HttpResponse(html_)


def base(request):
	num = random.randint(0,1000000)
	return render(request,"base.html" , {"rand" : num , "test" : " this values will dislplya at apge"})
	#return HttpResponse(html_)


def about(request):
	num = random.randint(0,1000000)
	return render(request,"about.html" , {"rand" : num , "test" : " this values will dislplya at apge"})
	#return HttpResponse(html_)

def defaultt(request):
	return render(request,"home.html",{})
