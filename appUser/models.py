from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   name = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to='profile')
   password = models.CharField(("Profil Şifre"), max_length=50, default=0000)
   password_active = models.BooleanField(("Şifre Aktif Et"), default=False)
   kid = models.BooleanField(("Çocuk Hesabı"), default=False)
   
   def __str__(self):
      return self.user.username + " " + self.name
   