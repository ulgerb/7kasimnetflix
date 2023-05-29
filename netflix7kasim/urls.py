
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from appMy.views import *
from appUser.views import *
from appVideo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage,name="indexPage"),
    
    # === USER ===
    path('login/', loginUser, name="loginUser"),
    path('logout/', logoutUser, name="logoutUser"),
    path('register/', registerUser,name="registerUser"),
    path('profile/', profilePage,name="profilePage"),
    path('account/<slug>/', accountPage,name="accountPage"),
    # path('profileDelete/<pid>/', profileDelete, name="profileDelete"),
    
    # === Video ===
    path('netflix/<slug>/', netflixPage,name="netflixPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
