from django.shortcuts import render

# Create your views here.

def indexPage(request):
   context = {"title": "Netflix"}
   return render(request,"index.html",context)



