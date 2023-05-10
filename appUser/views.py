from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# basriberkay@gmail.com

def loginUser(request):
   context={"title":"Giriş"}

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect("profilePage")
      else:
         messages.warning(request, "Kullanıcı adı veya şifre yanlış")
         return redirect("loginUser")
   
   return render(request,"user/login.html",context)

def registerUser(request):
   context={"title":"Kaydol"}

   if request.method == "POST":
      fname = request.POST.get("fname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")

      num=False
      upchar=False
      if password1==password2:
         for i in password1:
            if i.isupper() and not i.decimal():
               upchar = True
               break
         else:
            messages.warning(request, "Şifrede bir büyük harf olmak zorunda")
         for i in password1:
            if i.isdecimal():
               num = True
               break
         else:
            messages.warning(request, "Şifrede bir sayı olmak zorunda")
         
         if num and upchar and len(password1)>=6:
            if not User.objects.filter(username=username).exists():
               if not User.objects.filter(email=email).exists():
                  user = User.objects.create_user(first_name=fname, username=username,password=password1, email=email )
                  user.save()
                  return redirect("loginUser")
               else:
                  messages.warning(request, "Bu email zaten kullanılıyor")
                  return redirect("loginUser")
            else:
               messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor")
               return redirect("loginUser")
      else:
         messages.warning(request, "Şifreler aynı değil")
         return redirect("loginUser")
            
   return render(request,"user/register.html",context)

def profilePage(request):
   context={"title":"Profil"}
   return render(request,"user/profile.html",context)

def accountPage(request):
   context={"title":"Hesap Ayarları"}
   return render(request,"user/hesap.html",context)