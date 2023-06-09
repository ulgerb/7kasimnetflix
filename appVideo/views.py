from django.shortcuts import render, get_object_or_404
from appUser.models import Profile
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def netflixPage(request, slug=None):
   # Girişli profil sınırı
   context = {"title": "Netflix"}
   profile = get_object_or_404(Profile,slug=slug)
   profile.login_active = True
   profile.save()
   
   context.update({ "profile":profile })
   return render(request,"netflix.html",context)