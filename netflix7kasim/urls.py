
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
    path('register/', registerUser,name="registerUser"),
    path('profile/', profilePage,name="profilePage"),
    path('account/', accountPage,name="accountPage"),
    
    # === Video ===
    path('netflix/', netflixPage,name="netflixPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
