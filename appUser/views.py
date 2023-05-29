from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from appUser.models import *
from django.contrib.auth.decorators import login_required

# basriberkay@gmail.com
def loginUser(request):
   context={"title":"Giriş"}

   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(username=username, password=password)
      if user is not None:
         userinfo = get_object_or_404(UserInfo, user=user)
         if userinfo.sub_active:
            login(request, user)
            return redirect("profilePage")
         else:
            messages.warning(request, "Aboneliğinizi Devam Ettirimek İstiyormusunuz")
            return redirect("indexPage")
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

      contemail = False
      contusername = False
      num=False
      upchar=False
      if password1==password2:
         for i in password1:
            if i.isupper() and not i.isdecimal():
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
         
         if not User.objects.filter(username=username).exists():
            contusername = True
         else:
            messages.warning(request, "Bu kullanıcı adı zaten kullanılıyor")
         if not User.objects.filter(email=email).exists():
            contemail = True
         else:
            messages.warning(request, "Bu email zaten kullanılıyor")
         
         if num and upchar and len(password1)>=6:
            if contusername:
               if contemail:
                  user = User.objects.create_user(first_name=fname, username=username,password=password1, email=email )
                  user.save()
                  return redirect("loginUser")
         return redirect("registerUser")
      else:
         messages.warning(request, "Şifreler aynı değil")
         return redirect("registerUser")
            
   return render(request,"user/register.html",context)


@login_required(login_url="/login/")
def profilePage(request):
   context={"title":"Profil"}
   profiles = Profile.objects.filter(user=request.user)
   
   if request.method == "POST":
      submit = request.POST.get("submit")
      if submit == "profileAdd" and len(profiles) < 4:
         pname = request.POST.get("pname").strip(" ")
         image = request.FILES.get("image")
         password_active = request.POST.get("password_active")
         password = request.POST.get("password")
         kid = request.POST.get("kid")

         if pname == "":
               messages.warning(request, "Profil adı boş bırakılamaz")
               return redirect("profilePage")
         for i in pname:
            if i in " -*/+_.," or i is None:
               messages.warning(request, "Profil adı özel karakter içermemeli...")
               return redirect("profilePage")
         
         
         profileCr = Profile(name=pname, image=image, user=request.user, userinfo=request.user)
         if image is None:
            profileCr.image = "profile/patates.png"
         if password_active:
            if password.strip(" ") != "":
               profileCr.password_active = True
               profileCr.password = password
            else:
               messages.warning(request, "Profil şifresini girmediniz!!-------")
               return redirect("profilePage")
            
         if kid is not None:
            profileCr.kid = True
         
         profileCr.save()
         return redirect("profilePage")
   
      if submit == "profileLogin":
         password = request.POST.get("password")
         profileid = request.POST.get("profileid")
         profile = Profile.objects.get(id=profileid)
         
         if password == profile.password:
            return redirect("/netflix/" + profile.slug + "/")
         else:
            messages.warning(request, "Profile şifresi yanlış!!!")
            return redirect("profilePage")
            
   context.update({"profiles": profiles})
   return render(request,"user/profile.html",context)


@login_required(login_url="/login/")
def accountPage(request, slug):
   context={"title":"Hesap Ayarları"}
   profile = get_object_or_404(Profile, slug=slug)
   profiles = Profile.objects.filter(user=request.user)
 
   if request.method == "POST":
      submit = request.POST.get("submit")
      if submit == "profilDelete":
         password = request.POST.get("password")
         user = User.objects.get(username=request.user)
         if user.check_password(password):
            profilid = request.POST.get("profilid")
            profildel = profiles.get(id=profilid)
            profildel.delete()
            return redirect("profilePage")
         else:
            messages.warning(request, "Hesap şifresi yanlış!!!")
            return redirect("/account/"+slug+"/")
      elif submit == "profilUpdate":
         password = request.POST.get("password")
         user = User.objects.get(username=request.user)
         if user.check_password(password):
            profilid = request.POST.get("profilid")
            context.update({"profilid":profilid})
         else:
            messages.warning(request, "Hesap şifresi yanlış!!!")
            return redirect("/account/"+slug+"/")
      elif submit == "profilUpdateModal":
         
         image = request.FILES.get("image")
         pname = request.POST.get("pname")
         password = request.POST.get("password")
         password_active = request.POST.get("password-active")
         kid = request.POST.get("kid")
         profilid = request.POST.get("profilid")
         profilid = get_object_or_404(Profile, id=profilid) 
         if kid == "on":
            kid = True
         else:
            kid = False
            
         if password_active == "on":
            password_active = True
         else:
            password_active = False
         
         if image is not None:
            profilid.image = image
         profilid.name = pname
         profilid.password = password
         profilid.password_active = password_active
         profilid.kid = kid
         profilid.save()
         return redirect("/account/"+slug+"/")
      elif submit == "emailChange":
         email = request.POST.get("email")
         profile.user.email = email
         profile.user.save()
         return redirect("/account/"+slug+"/")
         
      elif submit == "telChange":
         tel = request.POST.get("tel")
         profile.userinfo.tel = tel
         profile.userinfo.save()
         return redirect("/account/"+slug+"/")
      elif submit == "passwordChange":
         password = request.POST.get("password")
         password1 = request.POST.get("password1")
         password2 = request.POST.get("password2")
         # user = User.objects.get(username= request.user)
         if request.user.check_password(password):
            if password1 == password2:
               request.user.set_password(password1)
               profile.userinfo.password = password1
               profile.userinfo.save()
               request.user.save()
         return redirect("/account/"+slug+"/")
         
     
   context.update({"profile": profile, "profiles": profiles})
   return render(request,"user/hesap.html",context)

@login_required(login_url='/login/')
def logoutUser(request):
   logout(request)   
   return redirect("indexPage")


# def profileDelete(request, pid):
#    print("pid============", pid)
#    profile = get_object_or_404(Profile, id=pid)
#    profile.delete()
#    return redirect("profilePage")