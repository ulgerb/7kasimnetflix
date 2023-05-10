from django.shortcuts import render

# Create your views here.


def netflixPage(request):
   context = {"title": "Netflix"}
   return render(request,"netflix.html",context)