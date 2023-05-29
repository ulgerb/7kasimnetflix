from django.shortcuts import get_object_or_404
from appUser.models import * 
from django.contrib.auth.decorators import login_required



def infoPage(request):
    
    if request.user.is_authenticated:
        context = {
            "userinfo": get_object_or_404(UserInfo, user = request.user),
        }
        return context
    else:
        return ""